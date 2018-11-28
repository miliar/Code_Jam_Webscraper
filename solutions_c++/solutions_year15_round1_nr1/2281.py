#include<fstream>
#include<cmath>

using namespace std;

int main(){
    long long t;
        ifstream cin("A-large-1.in");
    ofstream cout("A-large-1.out");
    cin>>t;
    for(long long e=0;e<t;e++){
        long long n;
        cin>>n;
        long long a[n];
        long long m1,m2;
        m1=m2=0;
        for(long long i=0;i<n;i++){
            cin>>a[i];
        }
        long long diff=0;
        for(long long i=1;i<n;i++){
            if(a[i]<a[i-1]){
            m1=m1+(a[i-1]-a[i]);
            }
            if(a[i-1]-a[i]>diff)diff=a[i-1]-a[i];
        }
        //m2
        //cout<<diff<<endl;
        long long plate=0;
        for(long long i=0;i<n-1;i++){
            plate=a[i];
            m2=m2+min(diff,plate);
            //plate=plate-min(diff,plate);
        }
        cout<<"Case #"<<e+1<<": "<<m1<<" "<<m2<<"\n";
    }
    cin.close();
    cout.close();
    return 0;
}
