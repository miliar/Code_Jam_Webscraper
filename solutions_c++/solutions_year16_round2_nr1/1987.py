#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <math.h>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

#define forn(i,n) for (int i=0;i<n;i++)
#define pb push_back



int main(){

  int t;

  cin>>t;

  forn (i,t){

    string num;

    int arr[30]={0};

    int phnum[11]={0};

    cin>>num;

    forn (j, num.size()){
      arr[ int (num[j]) -'A']++;
      //cout<<arr[ int (num[j]) -'A']
    }



    int temp=arr[int('Z')-'A'];

    while (temp>0){
      phnum[0]++;
      //cout<<"ze"<<endl;
      arr[int('Z')-'A']--;
      arr[int('E')-'A']--;
      arr[int('R')-'A']--;
      arr[int('O')-'A']--;
      temp=arr[int('Z')-'A'];
    }


     temp=arr[int('X')-'A'];

    while (temp>0){
      phnum[6]++;
      arr[int('S')-'A']--;
      arr[int('I')-'A']--;
      arr[int('X')-'A']--;
      //arr[int('O')-'A']--;
      temp=arr[int('X')-'A'];
    }


     temp=arr[int('G')-'A'];

    while (temp>0){
      phnum[8]++;
      arr[int('E')-'A']--;
      arr[int('I')-'A']--;
      arr[int('G')-'A']--;
      arr[int('H')-'A']--;
      arr[int('T')-'A']--;
      temp=arr[int('G')-'A'];
    }


     temp=arr[int('H')-'A'];

    while (temp>0){
      phnum[3]++;
      arr[int('T')-'A']--;
      arr[int('H')-'A']--;
      arr[int('R')-'A']--;
      arr[int('E')-'A']--;
      arr[int('E')-'A']--;
      temp=arr[int('H')-'A'];
    }


     temp=arr[int('R')-'A'];

    while (temp>0){
      phnum[4]++;
      arr[int('F')-'A']--;
      arr[int('O')-'A']--;
      arr[int('U')-'A']--;
      arr[int('R')-'A']--;
      temp=arr[int('R')-'A'];
    }


     temp=arr[int('F')-'A'];

    while (temp>0){
      phnum[5]++;
      arr[int('F')-'A']--;
      arr[int('I')-'A']--;
      arr[int('V')-'A']--;
      arr[int('E')-'A']--;
      temp=arr[int('F')-'A'];
    }


     temp=arr[int('V')-'A'];

    while (temp>0){
      phnum[7]++;
      arr[int('S')-'A']--;
      arr[int('E')-'A']--;
      arr[int('V')-'A']--;
      arr[int('E')-'A']--;
      arr[int('N')-'A']--;
      temp=arr[int('V')-'A'];
    }


     temp=arr[int('W')-'A'];

    while (temp>0){
      phnum[2]++;
      arr[int('T')-'A']--;
      arr[int('W')-'A']--;
      arr[int('O')-'A']--;
      //arr[int('O')-'A']--;
      temp=arr[int('W')-'A'];
    }
     temp=arr[int('O')-'A'];

    while (temp>0){
      phnum[1]++;
      arr[int('O')-'A']--;
      arr[int('N')-'A']--;
      arr[int('E')-'A']--;
      //arr[int('O')-'A']--;
      temp=arr[int('O')-'A'];
    }
     temp=arr[int('N')-'A'];

    while (temp>0){
      phnum[9]++;
      arr[int('N')-'A']--;
      arr[int('I')-'A']--;
      arr[int('N')-'A']--;
      arr[int('E')-'A']--;
      temp=arr[int('N')-'A'];
    }

    cout<<"Case #"<<i+1<<": ";

    forn (j,10){
      while (phnum[j]>0){
        cout<<j;
        phnum[j]--;
      }
    }

    cout<<endl;
  }

  return 0;
  }
