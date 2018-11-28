#include<bits/stdc++.h>

using namespace std;

int main()
{
    int cases;
    cin>>cases;
    for(int c = 1; c <= cases; c++)
    {
        int shyness;
        string s;
        cin>>shyness>>s;
        int sum = s[0] - '0';
        int friends = 0;
        for(int i = 1; i < s.size(); i++)
        {
            if(sum < i)
            {
                friends += (i-sum);
                sum += i-sum;


            }
            sum += s[i] - '0';
        }
        printf("Case #%d: %d\n", c, friends);

    }
    return 0;
}
