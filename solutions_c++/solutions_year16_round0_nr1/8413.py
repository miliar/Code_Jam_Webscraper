#include<iostream> 
#include<fstream> 
#include<string> 
#include<cstdio>
#include<sstream>
#include<algorithm>
#include<stdio.h>
#include<cstring>

using namespace std; 
 
bool isSubset(int arr1[], int arr2[], int m, int n)
{
    int i = 0;
    int j = 0;
    for (i=0; i<n; i++)
    {
        for (j = 0; j<m; j++)
        {
           if(arr2[i] == arr1[j])
              break;
        }
        
        if (j == m)
           return 0;
    }
     
    
    return 1;
}

int main() { 
int check[] = {0, 1, 2,3, 4, 5, 6, 7, 8, 9};
int sizecheck = sizeof(check)/sizeof(check[0]);
std::string x; 
std::string z;
long noc = 0;
int k=0;
int j=0;
long y;
int i;
int o;
long r = 0;
int comb[10000];
long foo = 0;
long cases = 0;
int N = 0;
cin >> cases;
for(foo=1; foo<=cases; foo++)
{
cin >> N;
memset(comb, 0, sizeof(comb));
noc = 0;
for(o=1; o<=9999999; o++)
{
y = 0;
y = N * o;
if(y == 0)
{
cout << "Case #" << foo << ": " << "INSOMNIA" << endl;
break;
}
std::string s = std::to_string(y);
int size = s.size();
int array[size];
for(i=1; i<=size; i++)
{
std::sort(std::begin(s), std::end(s));
int q = i-1;
z = s[q];
array[q] = stoi(z);
comb[noc] = array[q];
noc +=1;
}
int sizecomb = noc;
if(isSubset(comb, check, sizecomb, sizecheck)){
      cout << "Case #" << foo << ": " << y << endl;
      memset(array, 0, sizeof(array));
      break;
}
}
}
}
