#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
#define cin in
#define cout out
    int nbCas;
    cin>>nbCas;

    for(int c=1;c<=nbCas;c++) {
        long long int N;
        cin>>N;
        cout<<"Case #"<<c<<": ";

        if(N==0){
            cout<<"INSOMNIA"<<endl;
            continue;
        }

        vector<bool> seen(10,false);

        int restants = 10;
        int it;
        for(it=1;restants > 0;it++){
            long long int ntmp = N*it;
            while(ntmp != 0) {
                int digit = ntmp%10;
                if(!seen[digit]) {
                    restants --;
                    seen[digit]=true;
                }
                ntmp/=10;
            }
            if(restants==0) break;
        }
        cout<<it*N<<endl;

    }
}
