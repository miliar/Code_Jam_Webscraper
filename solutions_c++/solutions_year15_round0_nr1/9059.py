#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fstream>

using namespace std;

int main(){
    ofstream myfile;
    myfile.open("standing_ovation_large.txt");
    //FILE *f = fopen("standing_ovation_large.txt","a+")
    long long int t,smax,diff_max,sum,diff;
    string si;
    cin>>t;
    for(long long int i=1;i<=t;i++){
        cin>>smax;
        cin>>si;
        diff_max=0;
        sum=0;
        for(long long int j=0;j<=smax;j++){
            diff = sum -j;
            if(diff<diff_max)
                diff_max = diff;
            //cout<<int(si[j])<<"\n";
            sum += si[j] - '0';
        }
        //cout<<diff_max<<" "<<sum<<"\n";
        if(diff_max>=0)
            myfile<<"Case #"<<i<<": "<<0<<"\n";
        else
            myfile<<"Case #"<<i<<": "<<abs(diff_max)<<"\n";
    }
    myfile.close();
}
