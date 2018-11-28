#include<iostream>
#include<string>

using namespace std;

int main()
{
    int t,q,s_max,i,flag[10],fr,flag2[10];
    string s;
    cin >> t;
    for(q=0;q<t;q++)
    {
        cin >> s_max;
        cin >> s;
        if(s_max==0)
        {
            cout << "Case #" << q+1 << ": " << "0" << endl;
            continue;
        }
        fr=0;
        for(i=0;i<=s_max;i++)
        {
            flag2[i]=s[i]-48;
            if(i==0)
                flag[i]=flag2[i];
            else
                flag[i]=flag[i-1]+flag2[i];
            //cout << flag[i] << " ";
        }
        //cout << endl;
        for(i=1;i<=s_max;i++)
        {
            flag[i]=flag[i]+fr;
            if(flag[i-1]<i)
            {
                fr=fr+1;
                flag[i]=flag[i]+1;
                //cout << i << "i" << " " << flag[i] << " ";
            }
        }
        //cout << endl;
        cout << "Case #" << q+1 << ": " << fr << endl;
    }
    return 0;
}
