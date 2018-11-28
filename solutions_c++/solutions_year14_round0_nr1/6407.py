#include<iostream>
#include<iomanip>
#include<cstdlib>
#include<fstream>
using namespace std;
int main(){
    fstream fin,fout;
    fin.open("A-small-attempt0.in",ios::in);
    fout.open("Aout.txt",ios::out);
    int t;
    fin>>t;
    for(int u=0;u<t;u++){
        int gar,ans[2],get[4],compare[4],count=0,np=-1;
        bool check[4]={false,false,false,false};
        fin>>ans[0];
        if(ans[0]!=1) for(int i=0;i<(ans[0]-1)*4;i++) fin>>gar;
        for(int i=0;i<4;i++) fin>>get[i];
        if(ans[0]!=4) for(int i=0;i<(4-ans[0])*4;i++) fin>>gar;
        fin>>ans[1];
        if(ans[1]!=1) for(int i=0;i<(ans[1]-1)*4;i++) fin>>gar;
        for(int i=0;i<4;i++) fin>>compare[i];
        if(ans[1]!=4) for(int i=0;i<(4-ans[1])*4;i++) fin>>gar;
        /*for(int i=0;i<4;i++) fout<<get[i]<<" ";
        fout<<"\n";
        for(int i=0;i<4;i++) fout<<compare[i]<<" ";
        fout<<"\n";*/
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(get[i]==compare[j]) check[i]=true;
        for(int i=0;i<4;i++)
            if(check[i]){
                count++;
                np=i;
            }
        if(count==1) fout<<"Case #"<<u+1<<": "<<get[np]<<endl;
        else if(count>1) fout<<"Case #"<<u+1<<": Bad magician!\n";
        else fout<<"Case #"<<u+1<<": Volunteer cheated!\n";
    }
    return 0;
}
