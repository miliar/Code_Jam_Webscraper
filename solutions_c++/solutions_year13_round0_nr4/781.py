#ifdef __clang__
//to fix libstdc++ 4.4 and 4.5 in C++11 mode on cygwin
//refer to http://llvm.org/bugs/show_bug.cgi?id=13364
namespace std { struct type_info; }
#endif


#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>

#define FOR(i,N) for(i=0;i<(N);i++)
#define FORI(i,I,N) for(i=I;i<(N);i++)
#define FOREACH(i,N) for(auto i = N.begin();i<N.size(); i++)
//#define __DEBUG__

int i,j,k,l,m,n;
using namespace std;

int keys[10000];
int cases[200];
int cknum[200];
int casekeys[200][400];
vector<int> openorder;

//case: 0->close, 1->open
//key: 0->not use, 1->used
bool open_case(int cn, int c[], int cst[], int pc, int kn, int newkn, int k[], int kst[]){
    int i, j;
#ifdef __DEBUG__
    cout<<"kn="<<kn<<endl;
    cout<<"newkn="<<newkn<<endl;
    FOR(j,kn+newkn){
        cout<<k[j]<<",";
        cout<<kst[j]<<";";
    }
    cout<<endl;
    cout<<"cn="<<cn<<endl;
    FOR(j,cn){
        cout<<c[j]<<",";
        cout<<cst[j]<<";";
    }
    cout<<endl;
    FOR(j,openorder.size()){
        cout<<openorder[j]<<",";
    }
    cout<<endl;
    cout<<"------------"<<endl;
#endif
    bool allopen=true;
    FOR(i,cn){
        if(cst[i]==0){
           allopen=false;
           break;
        }
    }
    if(allopen) return true;

    FOR(i,cn){
        if(cst[i]==1) continue;
#ifdef __DEBUG__
    cout<<"try to open case:"<<i<<","<<c[i]<<endl;
#endif
        int jjj;
        if(i<pc&&newkn==0)continue;
        if(i<pc)jjj=kn;
        else jjj=0;
        FORI(j,jjj,kn+newkn){
            if(kst[j]==1) continue;
#ifdef __DEBUG__
    cout<<"try to use key:"<<j<<","<<k[j]<<endl;
#endif
            if(cst[i]==0 && kst[j]==0 && c[i] == k[j]){
#ifdef __DEBUG__
                cout<<"open case:"<<i<<","<<c[i]<<" with key:"<<j<<","<<k[j]<<endl;
#endif
                bool t;
                cst[i]=1;
                kst[j]=1;
                openorder.push_back(i);
#ifdef __DEBUG__
                cout<<"get keys:" << cknum[i]<<":";
#endif
                FOR(m,cknum[i]){
                    k[kn+newkn+m]=casekeys[i][m];
#ifdef __DEBUG__
                    cout<<kn+newkn+m<<","<<k[kn+newkn+m]<<";";
#endif
                    kst[kn+newkn+m]=0;
                }
#ifdef __DEBUG__
                cout<<endl;
#endif
                t=open_case(cn,c,cst,i,kn+newkn,cknum[i],k,kst);
                if(t) return true;
                else{
#ifdef __DEBUG__
    cout<<"open fail! pop!"<<endl;
#endif
                    cst[i]=0;
                    kst[j]=0;
#ifdef __DEBUG__
    cout<<"i="<<i<<",cst="<<cst[i]<<endl;
    cout<<"j="<<j<<",kst="<<kst[j]<<endl;
#endif
                    openorder.pop_back();
#ifdef __DEBUG__
    cout<<"put keys back:" << cknum[i]<<":";
#endif
                    FOR(m,cknum[i]){
#ifdef __DEBUG__
    cout<<kn+newkn+m<<","<<k[kn+newkn+m]<<";";
#endif
                        k[kn+newkn+m]=0;
                        kst[kn+newkn+m]=0;
                    }
#ifdef __DEBUG__
    cout<<endl;
#endif

                }
            }
        }
    }
#ifdef __DEBUG__
    cout<<"all closed cases cannot be open!"<<endl;
    cout<<"closed cases:";
    FOR(m,cn){
        if(cst[m]==0)
            cout<<m<<","<<c[m]<<"; ";
    }
    cout<<endl;
    cout<<"not used keys:"<<endl;
    FOR(m,kn+newkn){
        if(kst[m]==0)
            cout<<m<<","<<k[m]<<"; ";
    }
    cout<<endl;
    cout<<"------------"<<endl;
#endif
    return false;
}

int main()
{
	int casenum;
	cin >> casenum;
	FOR(i,casenum) {
        char c;
        int K,N;
        cout << "Case #" << (i+1) << ":";
        cin>>K;
        cin>>N;
        FOR(j,K){
            cin>>keys[j];
        }
        FOR(j,N){
            cin>>cases[j];
            cin>>cknum[j];
            FOR(k,cknum[j]){
                cin>>casekeys[j][k];
            }
        }

#ifdef __DEBUG__
        cout<<"\nK="<<K<<":";
        FOR(j,K){
            cout<<keys[j]<<",";
        }
        cout<<endl;
        cout<<"N="<<N<<":"<<endl;
        FOR(j,N){
            cout<<"case="<<j;
            cout<<":key="<<cases[j];
            cout<<":CK="<<cknum[j]<<":";
            FOR(k,cknum[j]){
                cout<<casekeys[j][k]<<",";
            }
            cout << endl;
        }
        cout << endl;
#endif
        bool t=true;
        int cst[200];
        int kst[10000];

        memset(kst,0,10000);
        FOR(j,K){
            kst[keys[j]]++;
        }
        FOR(j,N){
            FOR(k,cknum[j]){
                kst[casekeys[j][k]]++;
            }
        }
        int max=0,count=0;
        FOR(j,N){
            if(cases[j]>max) max=cases[j];
        }
#ifdef __DEBUG__
        cout<<"count:"<<endl;
#endif
        FORI(j,1,max+1){
            count=0;
            FOR(k,N){
                if(j==cases[k]) count++;
            }
#ifdef __DEBUG__
            cout<<j<<":"<<kst[j]<<":"<<count<<endl;
#endif
            if(count>kst[j]){
                t=false;
            }
        }
#ifdef __DEBUG__
        cout<<endl;
#endif
        if(t){

        memset(cst,0,200);
        memset(kst,0,10000);
        openorder.clear();
        t = open_case(N, cases, cst, -1, K, 0, keys, kst);
        }
        if(t){
            FOR(j,openorder.size()){
                cout<<" "<<openorder[j]+1;
            }
            cout<<endl;
        }
        else cout<<" IMPOSSIBLE"<<endl;

#ifdef __DEBUG__
        cout << endl;
        cout << endl;
#endif
    }
	return 0;
}
