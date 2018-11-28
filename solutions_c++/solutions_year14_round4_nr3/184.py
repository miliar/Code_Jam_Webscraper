#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cstring>
#include <cstdio>
#include <stdint.h>
#include <vector>
using namespace std;

const int MXN=10004;

int w, h, b;

const int MXB = 1000;

int bl[MXN][4];

const int MXD = 4096;
//
int dx[]={0,1, 0, -1};
int dy[]={1,0,-1, 0};

static void compress()
{
	typedef map<int, int> IntMap;
	IntMap Mp;
	for (int i=0; i<b; i++) {
		int p=bl[i][1];
		for (int t=0; t<=w; t++){
			Mp[p+t]=0;
			if (Mp[p-t] >= 0)Mp[p-t] = 0;
		}
		p=bl[i][3];
		for (int t=0; t<=w; t++){
			Mp[p+t]=0;
			if (Mp[p-t] >= 0)Mp[p-t] = 0;
		}
	}	
	IntMap::iterator it = Mp.begin();
	int id = 1;
	while (it != Mp.end()) {
		it->second = id;	
		id++;		
		it++;
	}
	h = id;
	for (int i=0; i<b; i++) {
		bl[i][1]=Mp[bl[i][1]];
		bl[i][3]=Mp[bl[i][3]];
	}
}
//uint16_t F[4194304][1024];

vector<vector<uint16_t> > F;
static void draw()
{
  F.resize(4194304);
  for (int j=0; j<=h; j++)F[j].assign(1024, 0);
  //memset(F, 0, sizeof(F));
  for (int i=0; i<b; i++) {
	for (int cy=bl[i][1]; cy <= bl[i][3]; cy++)
	for (int cx=bl[i][0]; cx <= bl[i][2]; cx++) {
		F[cy][cx+1] = w+100; 
	}
  }
  for(int i=0; i<=h; i++) {
	   F[i][0] = F[i][w+1] = w+100;
  }
}

static int solve()
{
  if (b == 0)return w;
  h++;
  compress();
  draw();
  /*for (int i=h; i>=0; i--)
  {
	for (int j=0; j<=w+1; j++) {
		if(F[i][j])fprintf(stderr, "@");
		else fprintf(stderr, ".");
	}
	fprintf(stderr, "\n");
	}*/
  int ans = 0;
  for (int k=1; k<=w; k++) {
	if (F[1][k])continue;
	//fprintf(stderr, "st: %d\n", k);
	int cd = 0;
	int cx = k;
	int cy = 1;
	while (cy > 0 && cy < h) {
	//	fprintf(stderr, "P: %d %d | %d\n", cx, cy, cd); 
		F[cy][cx] = k;
		for (int t=0; t<4; t++) {
			int tdir = (4 + cd - 1 + t) & 3; 
			int tx = cx+dx[tdir];
			int ty = cy+dy[tdir];
			//fprintf(stderr, "t: %d %d\n", tx, ty);
			int tv = F[ty][tx];
			if (tv == 0 || tv == k) {
				cy = ty;
				cx = tx;
				cd = tdir;
				break;			
			}
	    }
	}
	if (cy >= h)ans++;
  }
    /*for (int i=h; i>=0; i--)
  {
	for (int j=0; j<=w+1; j++) {
		if(F[i][j]>w)fprintf(stderr, "@");
		else if(F[i][j])fprintf(stderr, "%c", 'A'+(F[i][j]-1)%40);
		else fprintf(stderr, ".");
	}
	fprintf(stderr, "\n");
	}*/
  return ans;
}

int main()
{
  int t;
  cin >> t;
  for (int i=1; i<=t; i++) {
    cin >> w >> h >> b;
	for (int j=0; j<b; j++)
	for (int k=0; k<4; k++)cin >> bl[j][k];

    cout << "Case #" << i << ": " << solve() << "\n";
    cerr << "Case #" << i << ": " << solve() << "\n";
  }
  return 0;
}
