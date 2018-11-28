#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<iomanip>

using namespace std;

int T;

int r,c;
int t[1000];

int maze[20][20];

bool found;

//0=/, 1=\
//u,r,d,l
int dest(int x,int y, int dir) {
    if(1<=x&&x<=c&&1<=y&&y<=r) {

        if(dir==0) {
            if(maze[x][y]==0) {
                return dest(x+1,y,1);
            } else {
                return dest(x-1,y,3);
            }
        }


        if(dir==2) {
            if(maze[x][y]==0) {
                return dest(x-1,y,3);
            } else {
                return dest(x+1,y,1);
            }
        }

        if(dir==1) {
            if(maze[x][y]==0) {
                return dest(x,y-1,0);
            } else {
                return dest(x,y+1,2);
            }
        }

        if(dir==3) {
            if(maze[x][y]==0) {
                return dest(x,y+1,2);
            } else {
                return dest(x,y-1,0);
            }
        }
    } else {
        if(y<1) {
            return x;
        }
        if(x>c) {
            return c+y;
        }
        if(y>r) {
            return r+c+(c+1-x);
        }
        if(x<1) {
            return r+2*c+(r+1-y);
        }
        cout<<"!!!"<<endl;
    }
}


void brute(int x,int y) {
    if(found) return;
    if(y>r) {
        brute(x+1,1);
    } else {
        if(x<=c) {
            maze[x][y]=0;
            brute(x,y+1);
            maze[x][y]=1;
            brute(x,y+1);
        } else {
            bool good=true;
            for(int i=1;i<=c;i++) {
                if(dest(i,1,2)!=t[i]) {
                    good=false;
                }
                if(dest(c+1-i,r,0)!=t[c+r+i]) {
                    good=false;
                }
            }
            for(int i=1;i<=r;i++) {
                if(dest(c,i,3)!=t[c+i]) {
                    good=false;
                }
                if(dest(1,r+1-i,1)!=t[2*c+r+i]) {
                    good=false;
                }
            }
            if (good) {
                found=true;
                for(int y=1;y<=r;y++) {
                    for(int x=1;x<=c;x++) {
                        if(maze[x][y]==0) {
                            cout<<"/";
                        } else {
                            cout<<"\\";
                        }
                    }
                    cout<<endl;
                }
            }
        }
    }
}


int main() {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);


    cin>>T;
    for(int C=0;C<T;C++) {
        cin>>r>>c;
        int a,b;
        for(int i=0;i<2*(r+c);i+=2) {
            cin>>a>>b;
            t[a]=b;
            t[b]=a;
        }
        found=false;
        cout<<"Case #"<<C+1<<":"<<endl;
        brute(1,1);
        if(!found) {
            cout<<"IMPOSSIBLE"<<endl;
        }
    }
}
