 #include <bits/stdc++.h>
using namespace std;
 /*
  Mistakes -
   0) Dont rush to conclusion on seeing a question , keep yourself relaxed and go easy on ques .
   1) To see at each step if integer is not causing an error , best way is to use long long always.
   2) To see if my solution can be verified , if yes then do that .
   3) To see if my code can be simplified , if yes make it simple.
   4) If my code is wrong , dont be in a hurry to change to the code, first think for 2 min if any modification can be done to make it
      right.
   5) always typecast (int) arr.size() because   size_t does not support subtraction.
   6) Never use such expression   Int ct = max( ct ,left) ; (declartion should be done before assignment , absurd behaviour)
   7) Using long long for everything may cause Time Limit Exceeded some times , so better be sure
   8) appending at the end of the string takes too much time 339 Div2 - B
   9) Keep calm and Code.

 */
#define REP(i, a, b) for (int i = a; i <= b; i++)
#define FOR(i, n) for (int i = 0; i < n; i++)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define PI 3.1415926535897932385
#define uint64 unsigned long long
#define Int long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define ff first
#define ss second
#define bit(n) (1<<(n))
#define Last(i) ( (i) & (-i) )
#define sq(x) ((x) * (x))
#define INF INT_MAX
#define mp make_pair

int    main (  )
 {
   freopen("a.in", "r", stdin);
   freopen("a.out", "w", stdout);

   int t ;
   cin >> t ;

   while(t-- )
    {
      bool visit[10] ;
      FOR(i,10)visit[i]=false;

      Int n ;
      cin >> n ;
      if ( n  == 0 ){cout<<"INSOMNIA"<<endl;continue;}

      Int idx = 1 ;
      while( true )
       {
          Int tp =  n * idx ;
          string s = to_string(tp);
          FOR(i,s.length())visit[s[i]-'0'] = true;

          int j = 0 ;
          for( j = 0 ;j < 10 ;j++ )
            if(visit[j] ==  false)
                  break;

          if( j==10){ cout<<tp<<endl;break; }

         idx++;
       }


    }



 }
