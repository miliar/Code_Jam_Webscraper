#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <ctime>
#include <iterator>
#include <fstream>
using namespace std;
typedef long long ll;
#define sqr(a) ((a)*(a))

vector<vector<int> > red, blue, green;
int imgH, imgW;
const int INF=~(1<<31);
ifstream in;
ofstream out;
char *filename;
void parse(){
    QImage img(filename);
    red.assign (img.height (),vector<int>());
    green.assign (img.height(),vector<int>());
    blue.assign (img.height(),vector<int>());
    for(int i=0, k=0;k<img.height ();++k){
        for(int j=0;j<img.width ();j++,++i){
            red[k].push_back(qBlue(img.pixel (j, k)));
            green[k].push_back(qGreen(img.pixel (j, k)));
            blue[k].push_back(qRed(img.pixel (j, k)));
        }
    }
    while(red.size ()%8!=0){
        red.push_back (vector<int>());
        green.push_back (vector<int>());
        blue.push_back (vector<int>());
    }
    for(int i=0;i<red.size ();++i){
        while(red[i].size()%8!=0 || red[i].size()<red[0].size()){
            red[i].push_back(128);
            green[i].push_back(128);
            blue[i].push_back(128);
        }
    }

}
const int domainSize=8, rangeSize=4;
struct Domain{
    int a[rangeSize][rangeSize];
    int id;
    int sum, quas, div;
    Domain(int x, int y, char mode, int idd){
        id=idd;
        sum=0;
        quas=0;
        div=-1;
        if(mode==1){
            for(int i=0, ii=x;i<rangeSize;++i, ii+=2){
                for(int j=0,jj=y;j<rangeSize;++j,jj+=2){
                    int sum=0;
                    for(int i1=0;i1<2;++i1) for(int i2=0;i2<2;++i2) sum+=red[ii+i1][jj+i2];
                    a[i][j]=sum/4;
                }
            }
        }
        if(mode==2){
            for(int i=0, ii=x;i<rangeSize;++i, ii+=2){
                for(int j=0,jj=y;j<rangeSize;++j,jj+=2){
                    int sum=0;
                    for(int i1=0;i1<2;++i1) for(int i2=0;i2<2;++i2) sum+=green[ii+i1][jj+i2];
                    a[i][j]=sum/4;
                }
            }
        }
        if(mode==3){
            for(int i=0, ii=x;i<rangeSize;++i, ii+=2){
                for(int j=0,jj=y;j<rangeSize;++j,jj+=2){
                    int sum=0;
                    for(int i1=0;i1<2;++i1) for(int i2=0;i2<2;++i2) sum+=blue[ii+i1][jj+i2];
                    a[i][j]=sum/4;
                }
            }
        }
        for(int i=0;i<rangeSize;++i) for(int j=0;j<rangeSize;++j) sum+=a[i][j], quas+=sqr(a[i][j]);
    }
    Domain(){sum=0,quas=0, div=-1;}
    int getdiverse(){
        if(div!=-1) return div;
        int res=0, mid=sum/16;
        for(int i=0;i<rangeSize;++i) for(int j=0;j<rangeSize;++j){
            res+=sqr(a[i][j]-mid);
        }
        return div=res;
    }
};
struct Range{
    int a[rangeSize][rangeSize];
    int besti, bestn;
    int shift;
    int sum;
    double contrast;
    Range(int x, int y, char mode){
        besti=-1, bestn=INF, shift=0, sum=0;
        if(mode==1){
            for(int i=x,k=0;k<rangeSize;++i,++k){
                for(int j=y, h=0;h<rangeSize;++j,++h){
                    a[k][h]=red[i][j];
                }
            }
        }
        if(mode==2){
            for(int i=x,k=0;k<rangeSize;++i,++k){
                for(int j=y, h=0;h<rangeSize;++j,++h){
                    a[k][h]=green[i][j];
                }
            }
        }
        if(mode==3){
            for(int i=x,k=0;k<rangeSize;++i,++k){
                for(int j=y, h=0;h<rangeSize;++j,++h){
                    a[k][h]=blue[i][j];
                }
            }
        }
        for(int i=0;i<rangeSize;++i) for(int j=0;j<rangeSize;++j){
            sum+=a[i][j];
        }
    }
    Range(){besti=-1, bestn=INF, shift=0, sum=0; }
    void compare(const Domain &d){
        int n=rangeSize*rangeSize;
        int s1=0;
        for(int i=0;i<rangeSize;++i) for(int j=0;j<rangeSize;++j){
            s1+=d.a[i][j]*a[i][j];
        }
        double cur_contrast;
        if(n*d.quas!=sqr(d.sum))
            cur_contrast=((double)n*s1-sum*d.sum)/(n*d.quas-sqr(d.sum));
        else cur_contrast=0;
        if(cur_contrast>1.2) cur_contrast=1.2;
        if(cur_contrast<-1.2) cur_contrast=-1.2;
        int cur_shift=(sum-cur_contrast*d.sum)/(n+0.);
        if(cur_shift>255) cur_shift=255;
        if(cur_shift<-255) cur_shift=-255;
        int cur=0;
        for(int i=0;i<rangeSize;++i) for(int j=0;j<rangeSize;++j){
            cur+=sqr(cur_contrast*d.a[i][j]+cur_shift-a[i][j]);
        }
        if(cur<bestn){
            besti=d.id;
            bestn=cur;
            contrast=cur_contrast;
            shift=cur_shift;
        }

    }
    int getdiverse(){
        int res=0, mid=sum/16;
        for(int i=0;i<rangeSize;++i) for(int j=0;j<rangeSize;++j){
            res+=sqr(a[i][j]-mid);
        }
        return res;
    }
};
int n;
void compresse(char mode){
    vector<Domain> vec;
    vector<Range> ran;
    vector<int> sot;
    int idd=0;
    sot.push_back (0);
    for(int i=0;i<=imgH-domainSize;i+=4){
        for(int j=0;j<=imgW-domainSize;j+=4){
            Domain a(i, j, mode, idd++);
            int cu=a.getdiverse ();
            sot.push_back (cu);
            vec.push_back (a);
        }
    }
    int ingroup=300;
    if(sot.size ()<1000) ingroup=1000;
    if(sot.size ()<10000) ingroup=500;
    int qs=sot.size()/ingroup;
    vector<vector<Domain> > g(qs+1, vector<Domain>());
    sort(sot.begin (), sot.end ());
    for(int i=0;i<vec.size ();++i){
        int to=vec[i].getdiverse();
        int pos=lower_bound(sot.begin (), sot.end (), to)-sot.begin ();
        g[pos/ingroup].push_back(vec[i]);
    }
    for(int i=0;i<=imgH-rangeSize;i+=rangeSize){
        for(int j=0;j<=imgW-rangeSize;j+=rangeSize){
            Range a(i, j, mode);
            ran.push_back (a);
        }
    }
    for(int i=0;i<ran.size ();++i){
        int j=(lower_bound(sot.begin (), sot.end (), ran[i].getdiverse())-sot.begin ())/ingroup;
        for(int k=0;k<g[j].size();++k){
            ran[i].compare(g[j][k]);
            if(ran[i].bestn<20){
                break;
            }
        }
    }
    char w[3];
    int aa=ran.size ();
    w[0]=(((aa>>16)<<24)>>24);
    w[1]=(((aa>>8)<<24)>>24);
    w[2]=((aa<<24)>>24);
    out.write (w, 3);
    aa=imgH;
    w[0]=(((aa>>16)<<24)>>24);
    w[1]=(((aa>>8)<<24)>>24);
    w[2]=((aa<<24)>>24);
    out.write (w, 3);
    aa=imgW;
    w[0]=(((aa>>16)<<24)>>24);
    w[1]=(((aa>>8)<<24)>>24);
    w[2]=((aa<<24)>>24);
    out.write (w, 3);
    for(int i=0;i<ran.size ();++i){
        char wr[5];
        if(ran[i].shift<0) ran[i].besti|=(1<<23), ran[i].shift*=-1;
        unsigned int a=(((((unsigned int)ran[i].besti)<<8) | (ran[i].shift)));
        wr[0]=(a>>24);
        wr[1]=(((a>>16)<<24)>>24);
        wr[2]=(((a>>8)<<24)>>24);
        wr[3]=((a<<24)>>24);
        wr[4]=((unsigned char)(ran[i].contrast*100));
        out.write (wr, 5);
    }
}
vector<pair<int,pair<int,double> > > cha;
vector<vector<int> >  decompresse(char mode){

    vector<vector<int> > im(imgH, vector<int>(imgW,128));
    int tt=15;
    while(--tt){
        vector<Domain> vec;
        int idd=0;
        for(int i=0;i<=imgH-domainSize;i+=4){
            for(int j=0;j<=imgW-domainSize;j+=4){
                Domain a;
                for(int i3=0, ii=i;i3<rangeSize;++i3, ii+=2){
                    for(int j3=0,jj=j;j3<rangeSize;++j3,jj+=2){
                        int sum=0;
                        for(int i1=0;i1<2;++i1) for(int i2=0;i2<2;++i2) sum+=im[ii+i1][jj+i2];
                        a.a[i3][j3]=sum/4;
                    }
                }
                vec.push_back (a);
            }
        }
        int r=(mode-1)*n;
        for(int i=0;i<=imgH-rangeSize;i+=rangeSize){
            for(int j=0;j<=imgW-rangeSize;j+=rangeSize){
                for(int ii=0, k=i; ii<rangeSize;ii++,++k){
                    for(int jj=0,h=j; jj<rangeSize;jj++,++h){
                        im[k][h]=vec[cha[r].first].a[ii][jj]*cha[r].second.second+cha[r].second.first;
                        im[k][h]=max(im[k][h], 0);
                        im[k][h]=min(im[k][h], 255);
                    }
                }
                ++r;
            }
        }
    }
    return im;
}
void outt(vector<vector<int> > im1,vector<vector<int> > im2,vector<vector<int> > im3){
    imm=QImage(imgW, imgH, QImage::Format_RGB32);
    for(int i=0, k=0;k<imgH;++k){
        for(int j=0;j<imgW;j++,i+=3){
            imm.setPixel (j,k, qRgb(im1[k][j], im2[k][j], im3[k][j]));
        }
    }
    cout<<endl<<((float)clock())/CLOCKS_PER_SEC<<"  seconds"<<endl;
}
pair<int,pair<int,int> > toint(string a){
    int b[3]={0};
    int c[3]={1,1,1};
    for(int i=0, j=0;i<a.size()-1;++i){
        if(a[i]==' '){
            j++;
            continue;
        }else if(a[i]=='-'){
            c[j]*=-1;
        }else{
            b[j]*=10;
            b[j]+=(a[i]-'0');
        }
    }
    return make_pair(b[0]*c[0], make_pair(b[1]*c[1], b[2]*c[2]));
}

int main(){
    //freopen ("input.txt", "r", stdin);
    /*puts("press 1 to compress or 0 to decompress");
    int ty;
    cin>>ty;
    if(ty==1){
        out.open ("result.fract",ofstream::binary);
        filename= new char[100];
        puts("enter image name");
        string sf;
        scanf("\n");
        getline(cin, sf);
        filename=(char*)sf.c_str ();
        fflush(stdout);
        parse();
        imgH=red.size ();
        imgW=red[0].size();
        cout<<imgH<<' '<<imgW<<endl;
        compresse(1);
        compresse(2);
        compresse(3);
        cout<<endl<<((float)clock())/CLOCKS_PER_SEC<<"  seconds"<<endl;
        out.flush ();
    }else{*/
        freopen("rrr.txt", "r", stdin);
       // freopen("rr.txt", "w", stdout);
        cin>>n>>imgH>>imgW;
        scanf("\n");
        for(int i=0;i<3*n;++i){
            string s;
            getline(cin, s);
            pair<int,pair<int,int> > d=toint(s);
            int a=d.first, b=d.second.first;
            double c=d.second.second/1000.;
           // scanf("%d %d %lf\n", &a, &b, &c);
            cha.push_back(make_pair(a, make_pair(b,c)));
        }
       // in.open ("result.fract",ifstream::binary);
        vector<vector<int> > a1,a2,a3;
        a1=decompresse(1);
        a2=decompresse(2);
        a3=decompresse(3);
        outt(a1, a2, a3);
        imm.save ("result.bmp");
   // }
        return 0;
}

