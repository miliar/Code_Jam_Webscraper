#include <vector>
#include <algorithm>
#include <fstream>
#define LL long long int

using namespace std;

ifstream ein;
FILE * aus;
int TestCase;

void start()
{
	printf("%d\n", TestCase);
  LL result;
	// read test case
  LL N;
  ein >> N;
  vector<LL> a(N);
  vector<LL> b(N);
  for (int n=0;n<N;n++)
	{
		ein >> a[n];
		b[n] = a[n];
  }
  sort(b.begin(),b.end());
  int to,bo;
  to=N-1;
  bo=0;
  result=0;
  for (int n=0;n<N;n++)
  {
	  // look for b[n]
	  int cm;
	  for (int m=0;m<N;m++)
	  {
		 if (b[n]==a[m])
		 {
			 cm=m;
			 break;
		 }
	  }
	  int ml,mr;
	  // left
	  ml=cm-bo;
	  mr=to-cm;
	  if (ml<mr)
	  {
		  for (int k=cm;k>bo;k--)
		  {
			  swap(a[k],a[k-1]);
		  }
		  result+=ml;
		  bo++;
	  }
	  else
	  {
		  for (int k=cm;k<to;k++)
		  {
			  swap(a[k],a[k+1]);
		  }
		  result+=mr;
		  to--;
	  }
  }


/*
  int mxi;
  mxi = -1;
  for (int n=0;n<N;n++)
  {
	  b[n] = a[n];
	  if (mxi==-1)
	  {
		  mxi=n;
	  }
	  else
	  {
		  if (a[n]>a[mxi])
			  mxi=n;
	  }
  }

  result = N*N;
  int m;
  for (int m=mxi;m<N;m++)
  {
	  // 0..m, m..N-1 
	  int i,j;
	  LL f;
	  f=m-mxi;
	  for (i=0;i<m;i++)
	  {
		  for (j=i+1;j<m;j++)
		  {
			  if (a[i]>a[j])
			  {
				  f++;
			  }
		  }
	  }
	  for (i=m+1;i<N;i++)
	  {
		  for (j=i+1;j<N;j++)
		  {
			  if (a[i]<a[j])
			  {
				  f++;
			  }
		  }
	  }
	  if (f<result)
		  result = f;
	  if (m<N-1)
		  swap(a[m],a[m+1]);
  }
  // restore a
  for (int n=0;n<N;n++)
	  a[n]=b[n];

  for (m=mxi;m>=0;m--)
  {
	  // 0..m, m..N-1 
	  int i,j;
	  LL f;
	  f=mxi-m;
	  for (i=0;i<m;i++)
	  {
		  for (j=i+1;j<m;j++)
		  {
			  if (a[i]>a[j])
			  {
				  f++;
			  }
		  }
	  }
	  for (i=m+1;i<N;i++)
	  {
		  for (j=i+1;j<N;j++)
		  {
			  if (a[i]<a[j])
			  {
				  f++;
			  }
		  }
	  }
	  if (f<result)
		  result = f;
	  if (m>0)
		  swap(a[m],a[m-1]);
  }

  
  if (TestCase==82)
	  {
		  // altmeth
   int myints[] = {0,1,2,3,4,5,6,7,8,9};

  std::sort (myints,myints+10);
  int res;
  res=1000;
  do {
    
	// is updown?
		bool ok;
	for (int m=0;m<N;m++)
	{		
		ok=true;
		for (int i=0;i<m;i++)
		{
			if (b[myints[i]]>b[myints[i+1]])
				ok=false;
		}
		for (int i=m;i<N-1;i++)
		{
			if (b[myints[i]]<b[myints[i+1]])
				ok=false;
		}
	
	if(ok)
	{
		int fe=0;
	for (int i=0;i<N;i++)
		for (int j=i+1;j<N;j++)
		{
			if (myints[i]>myints[j])
				fe++;
		}

		if (fe<res)
			res=fe;
	}
	}
  } while ( std::next_permutation(myints,myints+N) );

  
  printf("case %d: %d %lld\n",TestCase,res,result);
  if (res!=result)
	  getchar();
	  */
  
	// output result
    fprintf(aus, "Case #%d: %lld\n", TestCase, result);     // %llu , %ll
}

void main()
{
	int NumTestCases;	
	ein.open("B-large.in");
	aus = fopen("ausgabe.txt","w");
	
	ein >> NumTestCases;
	for (TestCase = 1; TestCase <= NumTestCases; TestCase++)
		start();

	fclose(aus);
	ein.close();
}
