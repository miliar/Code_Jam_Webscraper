#include<iostream>
#include<fstream>
//#include<cstdlib>
//#include<vector>
using namespace std;

int main(){
   ifstream cin("C-small-9.in");
    ofstream cout("C-small-9.out");
    int t;
    cin>>t;
    int l,times;
    string s,g;
    char a[110][110];
    int pl[110][110];
    char c;
//cout<<(int)'1'<<" "<<(int)'i'<<" "<<(int)'j'<<" "<<(int)'k'<<endl;
    a['1']['1']='1';
    a['1']['i']='i';
    a['1']['j']='j';
    a['1']['k']='k';
    a['i']['1']='i';
    a['i']['i']='1';
    a['i']['j']='k';
    a['i']['k']='j';
    a['j']['1']='j';
    a['j']['i']='k';
    a['j']['j']='1';
    a['j']['k']='i';
    a['k']['1']='k';
    a['k']['i']='j';
    a['k']['j']='i';
    a['k']['k']='1';

    pl['1']['1']=1;
    pl['1']['i']=1;
    pl['1']['j']=1;
    pl['1']['k']=1;
    pl['i']['1']=1;
    pl['i']['i']=-1;
    pl['i']['j']=1;
    pl['i']['k']=-1;
    pl['j']['1']=1;
    pl['j']['i']=-1;
    pl['j']['j']=-1;
    pl['j']['k']=1;
    pl['k']['1']=1;
    pl['k']['i']=1;
    pl['k']['j']=-1;
    pl['k']['k']=-1;

    //cout<<a['1']['i']<<endl;
    for(int e=0;e<t;e++){
        cin>>l>>times;
        cin>>g;
        s.clear();
        for(int i=0;i<times;i++){
            s=s+g;
        }
        //multiply until i
        //cout<<s<<endl;
        //cout<<e<<endl;
        char cu;
        int pr;
        bool can;

        char fi[10100];
        int pl1[10100];
        //vector<int> start;

        //char se[1010];
        //int pl2[1010];
        //vector<int> ends;

         fi[0]=s[0];
         pl1[0]=1;

         for(int i=1;i<s.size();i++){
            pl1[i]=pl1[i-1]*pl[fi[i-1]][s[i]];
            fi[i]=a[fi[i-1]][s[i]];
            //if(fi[i]=='i'){start.push_back(i);}
            }


        can=0;
        for(int i=0;i<s.size();i++){
            if(fi[i]=='i' && pl1[i]==1){
                for(int br=i+1;br<s.size()-1;br++){
                    char sec=a[fi[i]][fi[br]];
                    int prsec=pl[fi[i]][fi[br]]*pl1[i]*pl1[br]*pl[fi[i]][fi[i]];

                    char the=a[fi[br]][fi[s.size()-1]];
                    int prthe=pl[fi[br]][fi[s.size()-1]]*pl1[br]*pl1[s.size()-1]*pl[fi[br]][fi[br]];
                    //cout<<prsec<<" "<<prthe<<endl;
                    if(sec=='j' && prsec==1 && the=='k' && prthe==1){can=1;goto A;}
                }
            }
        }



A:
        if(can)cout<<"Case #"<<e+1<<": YES\n";
        else cout<<"Case #"<<e+1<<": NO\n";
    }
        cin.close();
    cout.close();
    return 0;
}
