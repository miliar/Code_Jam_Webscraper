#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

string sheep(long long numb) {
        if(numb==0)
            return "INSOMNIA";
        else{
            long long num;
            int N=0;
            int tp[10];
            //indicator
            for(int i=0;i<10;i++){
                tp[i]=0;
            }
            while(tp[0]*tp[1]*tp[2]*tp[3]*tp[4]*tp[5]*tp[6]*tp[7]*tp[8]*tp[9]!=1){
                N++;
                num = N * numb;
                while(num>0){
                    tp[num%10] = 1;
                    num = num/10;
                }
            }
            return to_string(N * numb);
        }

}

int main()
{
        string str;
        getline(cin, str);
        int n = stoi(str);
        long long numb;
        for (int k = 0; k < n; k++) {
                scanf("%lld",&numb);
                cout << "Case #" << k+1 << ": " << sheep(numb) << endl;
	}

    return 0;
}
