#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include <iomanip> 
using namespace std;
//#define LARGE



int main() 
{
#if 1
#ifndef LARGE
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
#else
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
#endif
	int T;
	int count;
	double C,F,X;
	double psum =0;
	double sum =0.0, temp=0.0;
	scanf("%d", &T);

	for (int V = 1; V <= T; ++V) 
	{
	  //scanf("%f %f %f", &C, &F, &X);
	  cin>>C;
	  cin>>F;
	  cin>>X;
/*
	  cout<<std::setprecision(7)<<F<<endl;
	  cout<<fixed<<std::setprecision(7)<<X<<endl;*/
	  count=0;
	  //temp=0.0;
	  psum = double(X/2);
	  sum = double(C/2)+ X/(2+F);
	
	  while(sum < psum)
	  {
		  count = count+1;
		  //temp = sum;
		  psum=sum;
		  //calc new
		  /*
		  temp = 1/(2+F*count);
		  temp *= C;
		  temp =X/(2+F*count);
		  temp = X/(2+F*count+1);
		  */
		  sum = sum + C/(2+F*count) - X/(2+F*count)+ X/(2+F*(count+1));
		  //printf("psum=%5.7f\tsum=%5.7f\n",psum,sum); 
	  }
	  
	  
	 
	  printf("Case #%d: %5.7f\n", V,psum);
	}
	return 0;
}
