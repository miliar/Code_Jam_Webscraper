#include <iostream>
#include <iomanip>
#include <unordered_set>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
    freopen("output.txt","w",stdout);
    int num,i;
    cin >> num;
    for(i=0;i<num;i++)
    {
    	double c,f,x;
    	cin >> c >> f >> x;
    	double temp = x/2;
    	double best = 9999999;
    	int j = 0;
    	double cur = 0;
    	while(temp<=best)
    	{
    		best = temp;
    		cur += c/(2+j*f);
    		if(cur>best)break;
    		j++;
    		temp = cur+x/(2+j*f);
    	}
    	cout << "Case #" << i+1 << ": " << setprecision(7)<<setiosflags(ios::fixed)<<best <<endl;
    }
    return 0;
}