/*Code Developed By : Siddharth Sharma (B-Tech (C.S.E., IIIT-Delhi))*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("A-small-attempt1.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    long long int t_cases,case_ctr=1;
    cin>>t_cases;
    while(t_cases--)
    {
        string str;
        long long int length,i;
        cin>>length;
        cin>>str;
        long long int output=0,people_reqd_before=str[0]-'0';
        for(i=1;i<length+1;i++)
        {
            if(str[i]!='0')
            {
                if(people_reqd_before>=i)
                    people_reqd_before+=str[i]-'0';
                else
                {
                    output+=i-people_reqd_before;                            // 'i - people_reqd_before' : no. of people reqd. in crowd for current iteration
                    people_reqd_before += ( str[i] - '0' ) + ( i - people_reqd_before );
                }
            }
        }
        cout<<"Case #"<<case_ctr<<": "<<output<<endl;
        case_ctr++;
    }
    return 0;
}
