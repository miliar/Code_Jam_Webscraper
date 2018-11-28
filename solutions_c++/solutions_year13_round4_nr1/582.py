#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <queue>
#include <stack>

//#include <NTL/RR.h>
//using namespace NTL;

using namespace std;

/*
class mycomparison
{
  bool reverse;
  public:
  mycomparison(const bool& revparam=false)
  {reverse=revparam;}

  bool operator() (const int& lhs, const int&rhs) const
  {
    if (reverse) return (lhs>rhs);
    else return (lhs<rhs);
  }
};
*/


static int
cmpint(const void *p1, const void *p2)
{
  /* The actual arguments to this function are "pointers to
     pointers to char", but strcmp(3) arguments are "pointers
     to char", hence the following cast plus dereference */

  return (* (int * const *) p1)<( * (int * const *) p2);
}


struct passenger{
  int o;
  int e;
  int p;
};

static int cmppas(const void *p1, const void *p2)
{
  return (( (passenger * const ) p1)->o)>=( ( (passenger * const ) p2)->o);
}

static int cmpdown(const void *p1, const void *p2)
{
  return (( (passenger * const ) p1)->e)>=( ( (passenger * const ) p2)->e);
}


int main(){

	int i_cases;
	int N_cases;

	cin>>N_cases;

	priority_queue<int> cards;

	for(i_cases=0;i_cases<N_cases;i_cases++){

	  int N,M;
	  passenger pas[1000];
	  passenger down[1000];

	  cin>>N>>M;

	  int Total = 0;
	  for(int i=0;i<M;i++){
	    int o,e,p;
	    cin>>o>>e>>p;
	    
	    pas[i].o=o;
	    pas[i].e=e;
	    pas[i].p=p;

	    down[i]=pas[i];

	    int s = e-o;
	    Total += p*(s*N + (s-s*s)/2); //original profit by the city
	  }

	  qsort(pas,M,sizeof(pas[0]),cmppas);
	  qsort(down,M,sizeof(pas[0]),cmpdown);

	  passenger get_down_order[1000];
	  int lowest_price = 0;

	  int i=0,j=0;//i counter for pas;  j counter for down
	  stack<passenger> bus;//o for origen, p for passengers
	  while(i<M || j<M){
	    passenger newp;
	    if(i<M && (pas[i].o <= down[j].e)){ //handle get on
	      newp.o=pas[i].o;
	      newp.p=pas[i].p;
	      bus.push(newp);
	      i++;
	    }else{
	      while((down[j].p>0) && (bus.top().p<=down[j].p)){
		down[j].p -= bus.top().p;
		int s = (down[j].e - bus.top().o);
		lowest_price += bus.top().p * (s*N + (s-s*s)/2);
		bus.pop();
		if(bus.empty()){
		  break;
		}
	      }
	      if(!bus.empty()){
		int s = (down[j].e - bus.top().o);
		lowest_price += down[j].p * (s*N + (s-s*s)/2);
		bus.top().p -= down[j].p;
	      }
	      j++;
	    }
	   // cout<<pas[i].o<<endl;
	   // cout<<down[i].e<<endl;
	  }


	  int d=Total - lowest_price;

	  //printf("Case #%d: %f\n",i_cases+1,d);
	  cout<<"Case #"<<i_cases+1<<": "<<d<<endl;


	}
	return 0;

}
