#include <iostream>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

int pali(int no)
{
    int temp = no;
    int rem = 0;
    int rev = 0;
    while(temp > 0)
    {
        
        rem = temp%10;
        rev = rev*10;
        rev += rem;
        temp = temp/10;
        if(temp == 0)
        {
            break;
        }
    }
    if(rev == no)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main() {

    int i =0;
    int j =0;
    int k =0;
    int l =0;
        
    int cases = 0;
    cin >> cases;
    
    for(i=0; i<cases; i++)
    {
        int A = 0;
        int B = 0;
        
        int lower = 0;
        int higher = 0;
        int tots = 0;
        
        cin>>A>>B;
        
        lower = ceil(sqrt(A));
        higher = floor(sqrt(B));
        
        for(j=lower; j<=higher; j++)
        {
            if(pali(j))
            {
                if(pali(j*j))
                {
                    tots++;
                }
            }
        }
        cout<<"Case #"<<i+1<<": ";
        cout<<tots<<endl;
    }
    return 0;
}