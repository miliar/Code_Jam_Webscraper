#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    bool tab[10];
    for(int i=1; i<=t; i++)
    {
        int m;
        cin >> m;
        if(m==0)
            cout << "Case #" << i << ": INSOMNIA" << endl;
        else
        {
        	int n=m;
        	for(int a=0; a<10; a++)
        		tab[a]=false;
            while(true)
            {
                string x=to_string(n);
                for(int a=0; a<x.size(); a++)
                {
                	tab[int(x[a])-48]=true;
                }
                int d=0;
                for(int a=0; a<=9; a++)
                {
                	if(!tab[a])
                		d=1;
                }
                if(d==0)
                	break;
                n+=m;
            }
            cout << "Case #" << i << ": " << n << endl;
        }
    }
}
