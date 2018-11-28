/*
 * =====================================================================================
 *
 *       Filename:  consonants.cpp
 *
 *    Description:  Google code jam Problem A
 *
 *        Version:  1.0
 *        Created:  Sunday, 12/05/2013 17:26:35
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Terry Cheong. (terry182)
 *   Organization:  
 *
 * =====================================================================================
 */

#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int check(char c)
{ if (c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
	return 1;
  return 0;
}

int main()
{ long long int T;
	cin >> T;
  FILE* q;
  q = fopen("output.out","w");
  for (long long int c=1;c<=T;c++)
  { fprintf(q,"Case #%lld: ",c);
    printf("Case #%lld: ",c);
    string s; long long int n,ans=0;
  	cin >> s >> n;
    vector<long long int> startpoints;
    for (long long int i=0;i<=s.length()-n;i++)
    { long long int j;
	for (j=i;j<i+n;j++)
	{ if (check(s[j]))
		break;
	} 
      if (j==i+n)
      { startpoints.push_back(i);}
    }
    
    for (long long int i=0;i<startpoints.size();i++)
    { long long int point=startpoints[i];
	if (i==0)
	   ans+=point*(s.length()-point-n+1);
	else 
	   ans+=(point-startpoints[i-1]-1)*(s.length()-point-n+1);

     	ans+=(s.length()-point-n+1);
    }
    fprintf(q,"%lld\n",ans);
    printf("%lld\n",ans);
  }
return 0;}
