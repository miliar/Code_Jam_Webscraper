#include <iostream>
#include <iomanip>
#include <unordered_set>
using namespace std;

void sort(double *a, int num)
{
	int i,j;
	for(i=num-1;i>0;i--)
	{
		for(j=0;j<i;j++)
		{
			if(a[j]<a[i])
				swap(a[i],a[j]);
		}
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
    freopen("output.txt","w",stdout);
    int num,i;
    cin >> num;
    for(i=0;i<num;i++)
    {
    	int total;
    	cin >> total;
    	double a[1000],b[1000];
    	int j;
    	bool u[1000];
    	for(j=0;j<total;j++)
    	{
    		cin >> a[j];
    	}
    	for(j=0;j<total;j++)
    	{
    		cin >> b[j];
    		u[j] = false;
    	}
    	int s1 = 0,s2 = 0,p1=0,p2=0;
    	sort(b,total);
    	for(p1=0;p1<total;p1++)
    	{
    		bool win = false;
    		int can = -1;
    		for(p2=0;p2<total;p2++)
    		{
    			if(u[p2])continue;
    			if(b[p2]>a[p1])
    			{
    				win = true;
    				can = p2;
    			}
    			else
    				break;
    		}
    		if(win)
    		{
    			u[can] = true;
    		}
    		else
    		{
    			s2++;
    			for(p2=0;p2<total;p2++)
    			{
    				if(u[total-p2-1]==false)
    				{
    					u[total-p2-1] = true;
    					break;
    				}
    			}
    		}
    	}
    	sort(a,total);
    	p1 = 0;
    	for(p2=0;p2<total;p2++)
    	{
    		if(a[p1]>b[p2])
    		{
    			s1++;
    			p1++;
    		}
    	}
    	cout << "Case #" << i+1 << ": " << s1 << " " << s2 << " "<<endl;
    }

	return 0;
}