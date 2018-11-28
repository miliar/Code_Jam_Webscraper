#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

string solver(long long number) {
        if(number==0)
            return "INSOMNIA";
        else{
            long long num;
            int N=0;
            int exists[10];
            //indicator
            for(int i=0;i<10;i++){
                exists[i]=0;
            }
            while(exists[0]*exists[1]*exists[2]*exists[3]*exists[4]*exists[5]*exists[6]*exists[7]*exists[8]*exists[9]!=1){
                N++;
                num = N * number;
                while(num>0){
                    exists[num%10] = 1;
                    num = num/10;
                }
            }
            return to_string(N * number);
        }

}

int main()
{
        string str;
        getline(cin, str);
        int n = stoi(str);
        long long number;
        for (int k = 0; k < n; k++) {
                scanf("%lld",&number);
                cout << "Case #" << k+1 << ": " << solver(number) << endl;
	}

    return 0;
}

