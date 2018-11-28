#include<iostream>
#include<string>
#include<cstdio>
#include<limits>
#include<cmath>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

#define SMALL
//#define LARGE

int firstDiv(long long num)
{
    if(num % 2 == 0)
        return 2;
    for(int i = 3; i <= sqrt(num); i = i + 2)
    {
        if(num % i == 0)
            return i;
    }
    return -1;
}

long long convertToBase(char str[], int size, int base)
{
    long long num = 0, place = 1;
    for(int i = 0; i < size; i++)
    {
        if(str[i] == '1')
            num = num + place;
        place = place * base;
    }
    return num;
}

int main()
{

	#ifdef SMALL
		freopen("C-small-attempt6.in", "rt", stdin);
		freopen("C-small-attempt6.out", "wt", stdout);
	#endif

	#ifdef LARGE
		freopen("C-large.in", "rt", stdin);
		freopen("C-large.out", "wt", stdout);
	#endif
	
	int t;
	cin >> t;
	cout << "Case #1:" << endl;
	
	long long N, J, bin = 0, number[9], div[9], c = 0;
	cin >> N >> J;
	
	char str[N + 1];
	str[0] = '1';
	str[N - 1] = '1';
	str[N] = '\0';
	
	while(c < J)
	{
	    bool flag = true;
	    int temp = bin;
	    for(int i = 1; i < N - 1; i++)
	    {
	        if(temp % 2 == 0)
	            str[i] = '0';
	        else
	            str[i] = '1';
	        temp = temp / 2;
	    }
	    
	    for(int i = 0; i < 9; i++)
	    {
	        number[i] = convertToBase(str, N, i + 2);
	        div[i] = firstDiv(number[i]);
	        
	        if(div[i] == -1)
	        {
	            flag = false;
	            break;
	        }
	        
	        //cout << div[i] << " ";
	        
	    }
	    
	    if(flag == true)
	    {
	        for(int i = N - 1; i >= 0; i--)
	            cout << str[i];
	        
	        for(int i = 0; i < 9; i++)
	            cout << " " << div[i];
	        
	        cout << endl;
	        c++;
	    }
	    
	    bin++;
	}
	
	return 0;
}
