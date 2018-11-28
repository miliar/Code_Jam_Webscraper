#include <iostream>
#include <vector>
#include <fstream>
#include <cstring>

using namespace std;

int main(){

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w+",stdout);
    unsigned long long int n;
    cin>>n;
    bool t[10];
    bool ver;
    for(unsigned long long int i=0;i<n;i++) {
        unsigned long long int k;
        cin>>k;
        if(k==0) cout<<"Case #"<<i+1<<": INSOMNIA"<<'\n';
        else {
            for(unsigned long long int j=0;j<10;j++) t[j]=false;
            unsigned long long int compteur=1;
            ver=false;
            unsigned long long int copie;
            while(!ver) {
                 copie=k;
                copie*=compteur;
                while(copie>0) {
                    unsigned long long int first;
                    first=copie%10;
                    t[first]=true;
                    copie=(copie-first)/10;
                }
                compteur++;
                ver=true;
                for(unsigned long long int j=0;j<10;j++) if(t[j]==0) ver=false;
            }
            cout<<"Case #"<<i+1<<": "<<k*(compteur-1)<<'\n';
        }
    }
}
