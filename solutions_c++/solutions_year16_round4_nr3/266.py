#include <cstdio>
#include <algorithm>

using namespace std;

int T;
int r,c;
int a[400];

FILE *in, *out;

pair<pair<int,int>,pair<int,int> > inpos(int s) {
    if(s < c) return {{-1,s},{0,s}};
    s -= c;
    if(s < r) return {{s,c},{s,c-1}};
    s -= r;
    if(s < c) {
        s = (c-1)-s;
        return {{r,s},{r-1,s}};
    }
    s -= c;

    s = (r-1)-s;
    return {{s,-1},{s,0}};
}

pair<pair<int,int>,pair<int,int> > outpos(int s) {
    pair<pair<int,int>,pair<int,int> > r = inpos(s);
    swap(r.first,r.second);
    return r;
}

pair<pair<int,int>,pair<int,int> > trace(pair<pair<int,int>,pair<int,int> > p, int i) {
    if((p.second.first < 0) || (p.second.first >= r) || (p.second.second < 0) || (p.second.second >= c)) return p;

    int a(p.first.first-p.second.first);
    int b(p.first.second-p.second.second);
    bool typ(i&(1<<((p.second.first*c) + p.second.second)));

    swap(p.first,p.second);

    if(!typ) {
        p.second.first = p.first.first+b;
        p.second.second = p.first.second+a;
    } else {
        p.second.first = p.first.first-b;
        p.second.second = p.first.second-a;
    }

    return trace(p,i);
}

int main()
{
    in = fopen("C-small-attempt0.in","r");
    out = fopen("C-small.out","w");

    fscanf(in,"%d",&T);
    for(int t=1; t<=T; t++) {
        fscanf(in,"%d%d",&r,&c);
        for(int j=0; j<2*(r+c); j++) { fscanf(in,"%d",&a[j]); a[j]--; }

        bool sol(0);
        fprintf(out,"Case #%d:\n",t);

        for(int i=0; i<(1<<(r*c)); i++) {
            bool ok(1);
            for(int j=0; j<2*(r+c); j+=2) {
                if(trace(inpos(a[j]),i) != outpos(a[j+1])) {
                    ok = 0;
                    break;
                }
            }
            if(ok) {
                for(int k=0; k<r; k++) {
                    for(int j=0; j<c; j++) {
                        fprintf(out,((i&(1<<((k*c)+j))) ? "\\" : "/"));
                    }
                    fprintf(out,"\n");
                }

                sol = 1;
                break;
            }
        }

        if(!sol) {
            fprintf(out,"IMPOSSIBLE\n");
        }
    }

    fclose(in);
    fclose(out);

    return 0;
}
