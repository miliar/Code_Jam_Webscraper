#include <iostream>
#include <math.h>
//#include <stdlib.h>
using namespace std;

int atoi(char a)
{
    if(a == '0')
    {
        return 0;
    }
    if(a == '1')
    {
        return 1;
    }
    if(a == '2')
    {
        return 2;
    }
    if(a == '3')
    {
        return 3;
    }
    if(a == '4')
    {
        return 4;
    }
    if(a == '5')
    {
        return 5;
    }
    if(a == '6')
    {
        return 6;
    }
    if(a == '7')
    {
        return 7;
    }
    if(a == '8')
    {
        return 8;
    }
    if(a == '9')
    {
        return 9;
    }
}

int main() {
    
    short t, i;
    cin>>t;
    
    int smax, j, people = 0, friends = 0;
    
    for(i = 0; i < t; i++)
    {
        people = 0;
        friends = 0;
        cin>>smax;
        
        char s[smax];
        int s1[smax];
        
        for(j = 0; j <= smax; j++)
        {
            cin>>s[j];
            //cout<<"s[j] = "<<s[j]<<" "<<endl;
            
            s1[j] = atoi(s[j]);
            //cout<<"s1["<<j<<"] = "<<s1[j]<<" "<<endl;
            
            if(j > 0)
            {
                if(people < j)
                {
                    friends += (j - people);
                    people += (j - people);
                }
            }
            people += s1[j];
            
            //cout<<"people = "<<people<<endl;
            //cout<<"Friends = "<<friends<<endl;
        }
        
        cout<<"Case #"<<i+1<<": "<<friends<<endl;
    }
	return 0;
}