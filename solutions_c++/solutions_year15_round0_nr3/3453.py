#include <cstdio>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <map>
using namespace std;
int main()
{
	freopen("C-small-attempt1.in", "r" , stdin);
	freopen("d1.out", "w", stdout);
	int t,i,i1,j1,k1,x,cases=1,l;
    string letters,m,resi,resj,resk,m1,m2,m3,rep;
    bool flag=false;
    map<string, string> getvalue;
    getvalue["1i"]="i";
    getvalue["-1i"]="-i";
    getvalue["ii"]="-1";
    getvalue["-ii"]="1";
    getvalue["ij"]="k";
    getvalue["-ij"]="-k";
    getvalue["ik"]="-j";
    getvalue["-ik"]="j";
    getvalue["1j"]="j";
    getvalue["-1j"]="-j";
    getvalue["ji"]="-k";
    getvalue["-ji"]="k";
    getvalue["jj"]="-1";
    getvalue["-jj"]="1";
    getvalue["jk"]="i";
    getvalue["-jk"]="-i";
    getvalue["1k"]="k";
    getvalue["-1k"]="-k";
    getvalue["ki"]="j";
    getvalue["-ki"]="-j";
    getvalue["kj"]="-i";
    getvalue["-kj"]="i";
    getvalue["kk"]="-1"; 
    getvalue["-kk"]="1"; 
	scanf("%d",&t);
    while(t--){
        resi="";
        resj="";
        resk="";
        rep="";
        flag=false;
        m1="1";
        scanf("%d %d",&l,&x);
        cin>>letters;
        char first=letters[0];
        bool toloop=false;
        for(i=0;i<letters.length();i++){
            if(letters[i]!=first){
                toloop=true;
                break;
            }
        }
        rep=letters;
        for(i=1;i<x;i++)
            letters=letters+rep;
        l=letters.length();
        //cout<<"letters ="<<letters<<" length="<<l<<endl;
        if(toloop==true) {
            for(i1=0;i1<l;i1++){
                resi=getvalue[m1+letters[i1]];
                m1=resi;
                //cout<<"resi ="<<resi<<" ";
                if(resi=="i"){
                    m2="1";
                    for(j1=i1+1;j1<l;j1++) {
                        resj=getvalue[m2+letters[j1]];
                        m2=resj;
                        //cout<<"resj ="<<resj<<" ";
                        if(resj=="j"){
                            m3="1";
                            for(k1=j1+1;k1<l;k1++){
                                resk=getvalue[m3+letters[k1]];
                                m3=resk;
                                //cout<<"resk ="<<resk<<" ";
                            }
                            if(resk=="k"){
                                cout<<"Case #"<<cases<<":"<<" "<<"YES";
                                cout<<endl;
                                cases++;
                                flag=true;
                                break;
                            }
                            break;
                        }
                    }
                }
                if(flag==true)
                    break;
            }
        }
        if(flag==false){
            cout<<"Case #"<<cases<<":"<<" "<<"NO";
            cout<<endl;
            cases++;
        }
    }
    return 0;
}
