#include <fstream>
#include <iostream>
using namespace std;
int main()
{
    int t,n,x[26],c,i,j,pos,pos2,temp,temp2,count,flag;
    string str;
    ofstream op;
    op.open("output.in");

    ifstream ip;
    ip.open("A-large.in");

    ip>>t;
    for(c=1;c<=t;c++)
    {
        count=flag=0;
        ip>>n;
        str = "";
        for(i=0;i<n;i++)
        {
            ip>>x[i];
            count += x[i];
        }
        while(count)
        {
            pos = 0;
            temp = x[0];
            for(j=1;j<n;j++)
            {
                if(temp < x[j])
                {
                    temp = x[j];
                    pos = j;
                }
            }
            x[pos] = -1;
            pos2 = 0;
            temp2 = x[0];
            for(j=1;j<n;j++)
            {
                if(temp2 < x[j])
                {
                    temp2 = x[j];
                    pos2 = j;
                }
            }
            x[pos] = temp;
            if(temp==temp2 && temp!=0 )
            {
                count = count-2;
                if(count != 1)
                {
                    str = str + (char)(pos+65) + (char)(pos2+65) + " ";
                    x[pos]--;
                    x[pos2]--;
                }
                else
                {
                    str = str + (char)(pos+65) + " ";
                    x[pos]--;
                    count++;
                }
            }
            else if(temp>1)
            {
                count = count - 2;
                if(count != 1)
                {
                    str = str + (char)(pos+65) + (char)(pos+65) + " ";
                    x[pos] -= 2;
                }
                else
                {
                    str = str + (char)(pos+65) + " ";
                    x[pos] -= 1;
                }
            }
            else
            {
                str = str + (char)(pos+65) + " ";
                x[pos]--;
                count--;
            }
        }
        op<<"Case #"<<c<<": "<<str<<"\n";
    }
    ip.close();
    op.close();
    return 0;
}
