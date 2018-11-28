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


int T;
int main ()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	//auto it = v.begin()                //"it" has type v.begin(). We don't have to explicitly state type.
	
	cin>>T;
	
	
	forall(it, 1, T+1)
		{
			ll L, X;
			cin>>L>>X;
			
			char s[L];
			
			forall(i, 0, L)
				{
					cin>>s[i];
				}
		
						
			int pr = 1;
			int m = 1;
			int mi = 1;
			int mj = 1;
			int mk = 1;
			int count = 0;
			
			forall(j, 0, X)
				{
					forall(i, 0, L)
						{
							//cout<<j<<" "<<i<<" "<<s[i]<<" "<<pr<<" "<<m<<" "<<count<<endl;
							if(pr == 1)
								{
									//cout<<"pr1"<<endl;
									if(s[i] == 'i')
										{
											//cout<<"Ayi"<<endl;
											pr = 2;
											//cout<<pr<<
										}
									if(s[i] == 'j')
										{
											//cout<<"Ayj"<<endl;
											pr = 3;
										}
									if(s[i] == 'k')
										{
											//cout<<"Ayk"<<endl;
											pr = 4;	
										}
								
								}	
							
							else
								{
									if(pr == 2)
										{
											if(s[i] == 'i')
												{
													pr = 1;
													m *= -1;
												}
											if(s[i] == 'j')
												{
													pr = 4;
												}
											if(s[i] == 'k')
												{
													pr = 3;	
													m *= -1;
												}
											
										}		
									
									else
										{
											if(pr == 3)
												{
													if(s[i] == 'i')
														{
															pr = 4;
															m *= -1;
														}
													if(s[i] == 'j')
														{
															pr = 1;
															m *= -1;
														}
													if(s[i] == 'k')
														{
															pr = 2;	
														}
												
												}
											
											else
												{
													if(pr == 4)
														{
															if(s[i] == 'i')
																{
																	pr = 3;
																}
															if(s[i] == 'j')
																{
																	pr = 2;
																	m *= -1;
																}
															if(s[i] == 'k')
																{
																	pr = 1;	
																	m *= -1;
																}
															
														}
												}
									
										}
									
								}
							
							if(count == 0)
								{
									if(pr == 2)
										{
											count += 1;
											pr = 1;
											mi = m;
											m = 1;
										}
									
								}
							else
								{
									if(count == 1)
										{
											if(pr == 3)
												{
													count += 1;
													pr = 1;
													mj = m;
													m = 1;
												}
											
										}
									else
										{
											if(count == 2)
												{
													if(pr == 4)
														{
															count += 1;
															pr = 1;
															mk = m;
															m = 1;
														}
													
												}
										}
								}
							
							//cout<<pr<<" "<<m<<" "<<count<<endl;
						}
					
				}
			
						
			
			string ans;
			
			//cout<<pr<<" "<<mi<<" "<<mj<<" "<<mk<<" "<<m<<" "<<count<<endl;
			
			m = m*mi*mj*mk;
			
			if(count == 3)
				{
					if(pr == 1)
						{
							if(m == 1)
								{
									ans = "YES";
								}
							else
								{
									ans = "NO";
								}
						}
					else
						{
							ans = "NO";
						}	
					
				
				}
			else
				{
					ans = "NO";
				}
			
			
			
			
				
			cout<<"Case #"<<it<<": "<<ans<<endl;
		}
	
		
	return 0;
}

