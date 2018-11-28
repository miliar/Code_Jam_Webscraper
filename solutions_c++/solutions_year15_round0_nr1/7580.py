#include<iostream>
#include<fstream>

using namespace std;

int main(){
    long long int T;
    ifstream fin("A-large.txt");
    ofstream fout("asol.txt");
    fin>>T;
    for(long long int t = 1; t <= T; t++){
        long long int Smax;
        fin>>Smax;
        long long int sum = 0, ans = 0;
        for(int i = 0; i <= Smax; i++){
            char c;
            fin>>c;
            if(c-'0' > 0 && sum < i){
                ans += (i-sum);
                c += (i-sum);
		}
            sum += c-'0';
        }
        fout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
