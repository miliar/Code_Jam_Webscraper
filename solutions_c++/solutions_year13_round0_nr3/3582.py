#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<math.h>

using namespace std;

bool isPalindrome(int n){

int d = 0, num =n;

while(n/10 != 0){

//cout<<"LOOP "<<d<<"  "<<n<<" "<<n%10<<endl;

d += n%10;


d *= 10;

n /= 10;

//cout<<"LOOP "<<d<<"  "<<n<<endl;

}

d += n%10;



if(num == d)
    return 1;

return 0;

}



int main()
{
    freopen("C:/stream/C-small-attempt0.in", "r", stdin);
	freopen("C:/stream/Out-C-small.txt", "w+", stdout);

    int test, intOpen, intClose, intOpenTemp;

    cin>>test;

    for(int i = 0; i < test; i++){

    int n =0;

        cin>>intOpen>>intClose;

        intOpenTemp = sqrt(intOpen);
        intClose = sqrt(intClose);

        if(intOpenTemp * intOpenTemp <intOpen)
            intOpenTemp++;

        intOpen = intOpenTemp;

        for(int j = intOpen; j <= intClose; j++){

       // cout<<j<<endl;
            if(isPalindrome(j)){
                if(isPalindrome(j*j))
                    n++;
                }

            }

        cout<<"Case #"<<i+1<<": "<<n<<endl;
        }


	return 0;
}
