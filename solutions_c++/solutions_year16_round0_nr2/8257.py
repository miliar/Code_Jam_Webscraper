#include <iostream>
#include <vector>
#include <string>
using namespace std;
bool checkifcorrect(string s)
{
    for ( int i = 0; i< s.size(); i++)
    {
        if (s[i]== '-')
        {
            return false;
        }
    }
    return true;
}
char rev(char a)
{
    if (a == '-')
    {
        return '+';
    }
    else
    {
        return '-';
    }
}

int main()
{
 int t;
 cin>>t;
 int value = t;

 while(value--)
 {
     int val =0;
     string s;
     cin>>s;
     int l = s.size();
     int j = 0;
     for ( j= l - 1; j>= 0; j--)
     {
         if (s[j] == '-')
         {
             int k = 0;
             for( k = 0; k<j ; k++)
             {
                 if(s[k] == '-')
                 {
                     break;
                 }
             }
             if ( k != 0)
             {
                 //cout <<k;
                 //reverseString(s,0, k - 1);
                int i = 0;
                int w = k -1;
                for( ; i<( k / 2); i++, w--)
                {

                    char temp = s[w];
                    s[w] = rev(s[i]);
                    s[i] = rev(temp);
                    //cout<<s<<"Inside inner:"<<endl;
                }
                if ( k % 2 != 0)
                {
                    s[i] = rev(s[i]);

                }
                 val++;
             }
             //reverse from 0 to j in the string
             //reverseString(s, 0, j);

            int i = 0;
            int w = j;
            for( ; i<( (j+ 1) / 2); i++, w--)
            {

                char temp = s[w];
                s[w] = rev(s[i]);
                s[i] = rev(temp);

            }
            if ( (j%2) == 0)
            {
                s[ i] = rev(s[i]);
            }
            val ++;
            //cout<<s<<"After the final Reversal"<<endl;
         }
     }
     //cout<<s<<endl;
    if (checkifcorrect(s))
    {
         cout<<"Case #"<<t - value<<": "<<val<<endl;
    }
 }
}
