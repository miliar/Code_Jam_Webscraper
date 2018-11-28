#include <bits/stdc++.h>
using namespace std;
// const unsigned long long MAX = 10000000000;
vector<string> num;
vector<unsigned long long> baseRep;
// bool isComposite[MAX] = {0};

bool isComposite (unsigned long long n)
{
	unsigned long long sqr_root = sqrt(n), i;
	for (i=2; i<=sqr_root; ++i)
	{
		if (n%i == 0)
		{	
			return true;
		}
	}
	return false;
}

unsigned long long divisor(unsigned long long n)
{
	unsigned long long sqr_root = sqrt(n), i;
	for (i=2; i<=sqr_root; ++i)
	{
		if (n%i == 0)
		{	
			return i;
		}
	}
	return 1;
}

void getAllNumbers(int n)
{
    int min = 0, max = pow(2, n)-1, rem, j, count;
    for (int i=min; i<=max; ++i)
    {
        count = n;
        ostringstream os;
        os << 1;
        j = i;
        while (j > 1)
        {
            rem = j%2;
            j /= 2;
            os << rem;
            --count;
        }
        os << j;
        --count;
        while (count--)
        {
            os << 0;
        }
        
        os << 1;
        string str = os.str();
        reverse(str.begin(), str.end());
        num.push_back(str);
        // cout << str << endl;
    }
}

/*void setUpComposite()
{
    unsigned long long i, j;
    for (i=2; i<MAX; ++i)
    {
        if (!isComposite[i])
        {
            for (j=2; j*i <= MAX; ++j)
            {
                isComposite[j*i] = true;
            }
        }
    }
}*/


int main() {
    // setUpComposite();
	int t, n, m;
	cin >> t;
	for (int z=1; z<=t; ++z)
	{
	    cin >> n >> m;
	    cout << "Case #" << z << ":" << endl;
	    num.clear();
	    getAllNumbers(n-2);
	    int len = num.size();
	    for (int i=0; i<len && m>0 ; ++i)
	    {
	        // cout << "Checking " << num[i] << endl; 
	        baseRep.clear();
	        bool isCoinJam = true;
	        for (int j=2; j<=10; ++j)
	        {
	            // cout << "Checking base " << j << endl;
	            unsigned long long no = 0;
	            for (int k=0; k<n; ++k)
	            {
	                no += (pow(j, n-k-1)*((num[i])[k]-'0'));
	            }
	            if (!isComposite(no))
	            {
	                // cout << "Prime: " << no << endl;
	                isCoinJam = false;
	                break;
	            }
	            else
	            {
	                // cout << "Composite: " << no << endl;
	                baseRep.push_back(no);
	            }
	            // cout << "j = " << j << endl;
	        }
	        if (isCoinJam)
	        {
	            --m;
	            cout << num[i] << " ";
	            for (int j=2; j<=10; ++j)
	            {
	                // cout << baseRep[j-2] << " " ;
					cout << divisor(baseRep[j-2]) << " ";
	            }
	            cout << endl;
	        }
	    }
	}
	return 0;
}

