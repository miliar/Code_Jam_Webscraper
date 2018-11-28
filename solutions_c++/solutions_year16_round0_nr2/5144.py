#include<bits/stdc++.h>
#define INF 0x7fffffff

using namespace std;

int main()
{
int t;
    int cases =1;
    while(scanf("%d", &t)!=EOF)
    {
        while(t--)
        {
            printf("Case #%d: ", cases++);
            cin.ignore();
            string x;
            cin >> x;
            //cout << '\n' << x << "\n\n";

            int cnt = 0;
            while(count(x.begin(), x.end(), '-'))
            {
                string y = "";
                for(int i=0; i<x.size(); i++)
                {
                    if(i>0 && x[i]!=x[i-1])
                    {
                        for(int j=i; j<x.size(); j++)
                            y+= string(1,x[j]);

                        //cout << "oi" << i << "\n\n\n";
                        break;
                    }

                    y+= x[i] == '+' ? "-" : "+";
                }
                cnt++;
                //cout << "\n\n" << y << "\n\n";
                x = y;
            }

            printf("%d\n", cnt);
        }
    }
 return 0;
}
