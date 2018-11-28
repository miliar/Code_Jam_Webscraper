#include <fstream>
#include<iostream>
using namespace std;
#include<math.h>
long long power(long long a,long long b)
{
    long long answer = 1;
    while(b > 0)
    {
        if(b%2 == 1)
        {
            answer *= a;
        }
        a *= a;
        b = b>>1;
    }
    return answer;
}
int main()
{
    long long int number,n=1,k,c,s,t,j,y;
    /*ofstream outpu;
    outpu.open("out.txt");
    ifstream inpu;
    inpu.open("D-small-attempt1.in");
    inpu>>t;*/
    cin>>t;
    while(t--){
        /*inpu>>k>>c>>s;*/
        cin>>k>>c>>s;
      number = power(k,c);
        if(k==1)
        {
            cout<<"Case #"<<n<<": 1"<<"\n";
            /*outpu<<"Case #"<<n<<": 1"<<"\n";*/
        }
        else{
             cout<<"Case #"<<n<<": ";
             //outpu<<"Case #"<<n<<": ";
            y=(number-1)/(k-1);
            for(j=0;j<number;j=j+y)
            {
                //outpu<<j+1<<" ";
                cout<<j+1<<" ";
            }
            cout<<"\n";
            //outpu<<"\n";
        }
        n++;
    }
    /*inpu.close();
    outpu.close();*/
    return 0;
}
