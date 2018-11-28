#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <functional>
#include <utility>
//#include <tuple>
#include <cstdio>

//Useful Constants
#define INF									(int)1e9
#define EPS									1e-9


//Useful Hardware Instructions.

#define bitcount							__buitin_popcount						//Number of 1's in a binary.
#define gcd									__gcd									//Calculates gcd of pair of number (gcd 0,0 is undefined.)




//Fast Traversal

#define forall(i,a,b)						for(int i=a; i<b; i++)
#define foreach(it,c)						for( decltype  ( (c).begin()) it =  (c).begin(); it != (c).end() ; ++it )  //To access current element item you use *it.
#define all(a)								a.begin(), a.end()
#define in(elem,v)							( (v).find(elem) != (v).end() )			//Finds an elem in any stl container.
#define pb									push_back								// Adds elem to left of vector
#define fill(a,val)							memset(a,val,sizeof a)					//Initializes every elem of val to a. 
#define sz(a)								((int)(a.size()))						//gives size of stl container in int form (instead of size_t)


//Types

#define ULL									unsigned long long
#define ll									long long
#define vi									vector<int>


//Functions

#define maX(a,b)							( (a) > (b) ? (a) : (b) )
#define miN(a,b)							( (a) < (b) ? (a) : (b) )
#define checkbit (n,b)						( (n >> b) & 1 )            			// checks if b'th bit of n is true.
#define INDEX(arr,ind)						( lower_bound(all(arr),ind) - arr.begin())   // Gives position of first elem of sorted arr >= ind.


using namespace std;


//Auto memoziation

/*template <typename ReturnType, typename... Args>
std::function<ReturnType (Args...)> memoize(std::function<ReturnType (Args....)>)
{
	
	map<tuple<Args...>, ReturnType> cache;
	
	
	
	
	
	
	
	
}*/




/*ll fast_exp(ll base, ll exp)
	{
	    ll res=1;
	    while(exp>0) 
			{
		       if(exp%2==1) res=(res*base)%1000000007;
		       base=(base*base)%1000000007;
		       exp/=2;
		    }
	    return res%1000000007;
	}*/
	


int main ()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	//auto it = v.begin()                //"it" has type v.begin(). We don't have to explicitly state type.
	int T;
	cin>>T;
	
	forall(it, 1, T+1)
		{
			ll N, prev, mush, X, Y, max;
			cin>>N;
			ll A[N];
			X = 0;
			Y = 0;
			max = 0;
			
			cin>>mush;
			
			
			prev = mush;
			
			A[0] = mush;
			
			
			forall(i, 1, N)
				{
					cin>>mush;
					A[i] = mush;
					if(prev>mush)
						{
							X += prev - mush;
							
							if((prev - mush) > max)
								{
									max = prev - mush;
								}
							
						}
					
					prev = mush;
					
				}
			
			forall(i, 0, N-1)
				{
					if(A[i]<max)
						{
							Y += A[i];
						}
					else
						{
							Y += max;
						}
				}
			
			cout<<"Case #"<<it<<": "<<X<<" "<<Y<<endl;
		}
	
	
	
	
		
	return 0;
}

