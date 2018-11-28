#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cassert>
#include<climits>

using namespace std;

vector<long long> candidates;

bool isPalindrome(long long int n){
    long long int orig = n;
    long long int rev  = 0;
    while( n > 0){
        rev= rev*10 + n%10;
        n/=10;
    }
    if(rev == orig)
        return true;
    return false;
}

void preprocess(){
    vector <long long> temp;
    for( long long int i = 1L; i <= 10000000L; i++)
        if(isPalindrome(i)){
            //cerr<<i<<"is palin ";
            temp.push_back(i*i);
        }
    for( int i = 0; i < temp.size(); i++)
        if(isPalindrome(temp[i])){
            //cerr<<temp[i]<<"is fair sqr";
            candidates.push_back(temp[i]);
        }
    candidates.push_back(LONG_LONG_MAX);
    sort(candidates.begin(), candidates.end());
    //cerr<<"temp.size="<<temp.size()<<" candidates.size()="<<candidates.size()<<"\n";
}

int binarySearch(vector<long long> ar ,long long k){
    int lo = 0, hi = ar.size()-1;
   while (lo < hi){
        int mid = lo + (hi-lo)/2;
      if (k < ar[mid])
         hi = mid;
      else
         lo = mid+1;
   }
   assert(ar[lo]>k);      // p(x) is false for all x in S!
   return lo;        // lo is the least x for which p(x) is true
}
int main(){
    int t=1,T;
    preprocess();
    scanf("%d",&T);
    while(t <= T){
        long long A, B;
        scanf("%lld%lld",&A,&B);
        int a = binarySearch(candidates,A-1);
        int b = binarySearch(candidates,B);
        //cerr<<b<<" "<<a<<endl;

        printf("Case #%d: %d\n",t,b-a);
        t++;
    }
}
