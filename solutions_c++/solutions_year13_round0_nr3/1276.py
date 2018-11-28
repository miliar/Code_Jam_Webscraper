#include<iostream>
#include<conio.h>
#include<vector>
#include<math.h>
#include<string>
#include<map>
using namespace std;
bool isPalin(long long int inp) {
      char z[1000];
      (void) sprintf(z, "%lld", inp);
      int i = 0;
      int j = strlen(z) - 1;
      while(i<j) {
                 if(z[i] != z[j]) {
                         return false;
                 }
                 i++;
                 j--;
      }
      return true;
}
bool isFairAndSquare(long long int i, map<long long int, int> &p) {
     double sqd = sqrt(i);
     long long int sq = (long long int)floor(sqd);
     if(sqd==sq) {
                       if(p[sq]!=1) {
                              bool ispsq;
                              if(p[sq] == 0) {
                                       ispsq = isPalin(sq);
                                       if(ispsq) {
                                                 p[sq] = 2;
                                       } else {
                                                 p[sq] = 1;
                                       }
                              }
                              bool isp;
                              if(p[sq] == 2) {
                                       isp = isPalin(i);
                                       if(isp) {
                                               p[i] = 2;
                                               return true;
                                       }else {
                                               p[i] = 1;
                                       }
                              }
                                               
                       }
                                       
     }
     return false;
}
int searchBeg(vector<long long int> fs, long long int num) {
    int i = 0;
    int j = fs.size() - 1;
    while(i<=j) {
               int mid = (i+j)/2;
               if(fs[mid] == num) {
                          return mid - 1;
               } else if(fs[mid] < num && fs[mid+1] > num) {
                          return mid;
               } else if(fs[mid]<num) {
                      i = mid + 1;
               } else {
                      j = mid - 1;
               }
    }
    cout<<"error "<<num<<" ";
    return 0;
}
int searchEnd(vector<long long int> fs, long long int num) {
    int i = 0;
    int j = fs.size() - 1;
    while(i<=j) {
               int mid = (i+j)/2;
               if(fs[mid] == num) {
                          return mid;
               } else if(fs[mid] < num && fs[mid+1] > num) {
                          return mid;
               } else if(fs[mid]<num) {
                      i = mid + 1;
               } else {
                      j = mid - 1;
               }
    }
    cout<<"error "<<num<<" ";
    return 0;
}
int main()
{
    vector<long long int> v;
    for(long long int i =1; i<pow(10,7) + 5;i++) {
             if(!isPalin(i)) {
                             continue;
             } else {
                    long long int sqNum = i*i;
                    if(isPalin(sqNum)) {
                                       v.push_back(sqNum);
                    }
             }
    }
    int count = 0;
    cin>>count;
    int q = 0;
    while(q<count) {
                   cout<<"Case #"<<q+1<<": ";
                   long long int start,end;
                   cin>>start;
                   cin>>end;
                   int begCount = searchBeg(v, start);
                   int endCount = searchEnd(v,end);
                   cout<<endCount - begCount<<endl;
                   q++;
    }
    return 0;
}
