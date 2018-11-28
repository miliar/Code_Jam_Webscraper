#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 2200;
const int inf = 0x7fffffff;

struct rt{
	int stop, p;
	};

rt stoteles[MAXN];
rt stot[MAXN];

bool cmp(const rt & a, const rt & b){
	if(a.stop == b.stop)
		return a.p > b.p;
	return a.stop < b.stop;
	}

int cost(int fr, int to, int n){
	int k = to - fr;
	return (k*n - ((k)*(k-1) / 2) ); 
	}

int main(){
	int testcases;
	scanf("%d", &testcases);
	
	for(int testcase = 0; testcase < testcases; testcase++){
		int n, m;
		int fr, to, many;
		int st = 1;
		scanf("%d%d", &n, &m);
		
		int firstcost = 0;
		int actualcost = 0;
		
		for(int i = 0; i < m; i++)
			scanf("%d%d%d", &fr, &to, &many),
			stot[2*i    ] = (rt){fr, many},
			stot[2*i + 1] = (rt){to, -many},
			firstcost += many * cost(fr, to, n);
			
		sort(stot, stot + 2*m, cmp);
		
		int actm = 0;
		stoteles[actm].p = stot[0].p;
		stoteles[actm].stop = stot[0].stop;
		
		for(int i = 1; i < 2*m; i++)
			if(stot[i].stop == stoteles[actm].stop)
				stoteles[actm].p += stot[i].p;
			else
				stoteles[++actm].p = stot[i].p,
				stoteles[actm].stop = stot[i].stop;
		m = actm+1;
		
		//~ for(int i = 0; i < 2*m; i++)
			//~ cout << stoteles[i].stop << " " << stoteles[i].p << endl;
		
		while(st != -1){
			//~ for(int i = 0; i < m; i++)
			//~ cout << stoteles[i].stop << " " << stoteles[i].p << endl;
			//~ cout << endl;
			//~ sort(stoteles, stoteles + m, cmp);
			st = -1;
			for(int i = 0; i < m; i++)
				if(stoteles[i].p > 0){
					st = i;
					break;
					}
					
			//~ cout  << " "<< st << endl;
			
			if(st == -1)
				break;
			
			int bal = stoteles[st].p, end = -1;
			int cs = bal;
			
			for(int i = st + 1; i < m; i++){
				bal += stoteles[i].p;
				
				//~ cout << bal << endl;
				if(bal <= 0){
					end = i;
					break;
					}
				cs = min(cs, bal);
				}
			//~ cout << end << endl;
			if(end == -1)
				break;
			
			//~ int cs = min(stoteles[st].p, -stoteles[end].p);
			actualcost += cs * cost(stoteles[st].stop, stoteles[end].stop, n);
			//~ cout << "cs: " <<cs << endl;
			stoteles[st].p -= cs;
			stoteles[end].p += cs;
			
			
			}	
		//~ cout << firstcost << endl << actualcost << endl;
		printf("Case #%d: %d\n", testcase+1, firstcost-actualcost);
		}
	
	
	return 0;
}
