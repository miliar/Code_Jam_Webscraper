#include<cstdio>
#include<vector>
#include<set>
#include<utility>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>

using namespace std;
long long fairsq[] = {1 ,4 ,9 ,121 ,484 ,10201 ,12321 ,14641 ,40804 ,44944 ,1002001 ,1234321 ,4008004 ,100020001 ,102030201 ,104060401 ,121242121 ,123454321 ,125686521 ,400080004 ,404090404 ,10000200001 ,10221412201 ,12102420121 ,12345654321 ,40000800004 ,1000002000001 ,1002003002001 ,1004006004001 ,1020304030201 ,1022325232201 ,1024348434201 ,1210024200121 ,1212225222121 ,1214428244121 ,1232346432321 ,1234567654321 ,4000008000004 ,4004009004004};

int main()
{
	long long t,i,j,a,b,m=1,ans,check;
    char ch;
	FILE *ifp, *ofp;
    char outputFilename[] = "output_fsq.txt";

    ifp = fopen("input_fsq.in", "r");
	ofp = fopen(outputFilename, "w");

	fscanf(ifp, "%lld", &t);

	while(t--)
	{
	    fscanf(ifp,"%c", &ch);
        fscanf(ifp,"%lld%lld", &a, &b);
		ans=0;
		check = 0;
        for(i=0; i<39; i++)
        {
            if(fairsq[i] >= a)
            {
                check=1;
                for(j=i; b >= fairsq[j] && j<39;  j++);
                break;
            }
        }
        if(check == 0)
            ans = 0;
        else
          ans = j-i;
        if(fairsq[j]==b)
           ans++;
		fprintf(ofp, "Case #%lld: ", m);
		fprintf(ofp, "%lld\n", ans);
        m++;
	}

	return 0;
}
