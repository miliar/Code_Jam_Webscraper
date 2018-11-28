#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int t;
    cin>>t;
    for(int T=1; T<=t; T++){
        int n;
        cin>>n;
        vector<double> nao(n), ken(n);
        for(int i=0; i<n; i++) cin>>nao[i];
        for(int i=0; i<n; i++) cin>>ken[i];
        sort(ken.begin(), ken.end());
        sort(nao.begin(), nao.end());
        int dec=0, naoCounter=0, kenCounter=0, kenUp=n-1;
        cout<<"Case #"<<T<<": ";

        while(naoCounter<n && kenCounter<=kenUp ){
            if(nao[naoCounter]<ken[kenCounter]) {naoCounter++; kenUp--;}
            else {dec++; kenCounter++; naoCounter++;}

        }
        cout<<dec<<" ";

        naoCounter=0; kenCounter=0;
        while(naoCounter<n && kenCounter<n ){
            if(nao[naoCounter]<ken[kenCounter]) {naoCounter++; kenCounter++;}
            else kenCounter++;
        }
        cout<<n-naoCounter<<endl;


    }
    return 0;
}
