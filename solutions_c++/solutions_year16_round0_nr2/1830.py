#include <iostream>
#include <iomanip>

//#define _DEBUG_
//#ifdef _DEBUG_
//#endif

using namespace std;

void flip(char *s, int l, int r)
{
#ifdef _DEBUG_
   cout << " flip: " << l << ' ' << r ;
#endif
   while(l<=r)
   {
      if(s[l]==s[r])
      {
         if(s[l]=='+')
            s[l]=s[r]='-';
         else
            s[l]=s[r]='+';
      }
      l++; r--;
#ifdef _DEBUG_
   cout << " flip: " << l << ' ' << r ;
#endif
   }
}

int cntChr(char *s, int l, int r)
{
   char c;
   int i;

   c = s[l];
   for(i=l+1; i<=r  && c==s[i]; i++)
      ;
   return i-l;
}

int main()
{
	int T;

	cin >> T;
	for(int t=1; t<=T; t++){
		/************************************
		*	Input Data
		*************************************/
		char S[101];
		cin >> S;
		/************************************
		*	Solve the Problem
		*************************************/
		int l=0, r=strlen(S)-1, count=0;
		while(l<=r)
		{
#ifdef _DEBUG_
                   cout << " S:" << S << l << ' ' << r;
#endif

		   if(S[r]=='+')
		      r--;
		   else
		   {
		      int left_cnt = cntChr(S,l,r);
                      l+=left_cnt;
                      count++;
		      if(S[l-left_cnt]=='-')
		      {
		         flip(S,l,r);
		      }
		   }
#ifdef _DEBUG_
                   cout << endl << " S:" << S << "count: " << count << endl;
#endif
		}
		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << t << ": " << count << endl;
		
	}

	return 0;
}
