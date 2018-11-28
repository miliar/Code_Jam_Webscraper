#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <string.h>
#include <string>

#define MAX_STR_LEN 10000
#define MAX_TABLE (4+1)
#define YES 1
#define NO 0
const char *yesNo[]={"NO", "YES"};
typedef struct Dijkstra_tag
{
    int len;
    int xRep;
    int first;
    int second;
    int size;
    char *instr;
    char *str;
} Dijkstra;
typedef enum{
 H_ONE, //0
 H_I,   //1
 H_J,   //2
 H_K,   //3
 V_ONE, //4
 V_I,   //5
 V_J,   //6
 V_K    //7
} tabVal;
//int table[MAX_TABLE][MAX_TABLE]={{V_ONE, V_I, V_J,V_K},{V_I, -V_ONE, V_K, -V_J}, {V_J, -V_K, -V_ONE, V_I},{V_K, V_J, -V_I, -V_ONE}};
/*
 * 1 = 1
 * i = 2
 * j = 3
 * k = 4
 */
int table[MAX_TABLE][MAX_TABLE]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2}, {0,4,3,-2,-1}};
using namespace std;
void IntTokenize(string word, int *len, int*xRep);
void ExpandString(Dijkstra *set);
void ClearSet(Dijkstra *set);
void ClearAndFreeSet(Dijkstra *set);
int quaternionPossible(Dijkstra *set);
int Mul(char *str, int begin, int end);
int main(int argc, char **argv) {
    ifstream in (argv[1]);
    ofstream out (argv[2]);
    string row;
    Dijkstra set;
    int noOfcases;
    int tmp=0;

    ClearSet(&set);
    getline(in, row);
    noOfcases=atoi(row.c_str());
    for(int i=1;i<=noOfcases;i++)
    {
        /* Initialize the variables */
        getline(in, row);
        IntTokenize(row, &(set.len), &(set.xRep));

        set.instr = (char *)malloc(set.len+1);
        memset(set.instr,0,set.len+1);
        getline(in, row);
        strncpy(set.instr,row.c_str(), set.len);
        /* Expand String */
        ExpandString(&set);
        tmp = quaternionPossible(&set);
        cout<<"Case #"<<i<<": "<<yesNo[tmp]<<endl;
        out<<"Case #"<<i<<": "<<yesNo[tmp]<<endl;

        ClearAndFreeSet(&set);
    }


    return 0;
}

int Mul(char *str, int begin, int end)
{
 int i;
 int prod=1;
 int tmp;
 int sign=0;
 
 for(i=begin;i<end;i++)
 {
     tmp = str[i]-'i'+2;
     prod = table[prod][tmp];
     if (prod<0)
     {
         sign++;
         prod*=(-1);
     }
 }
 if (sign%2) prod*=-1;
 
 return prod;
}
#if 0
int Mul(char a, char b)
{
 return table[a-'i'+2][b-'i'+2];
}
#endif
int quaternionPossible(Dijkstra *set)
{
    bool exit = false;

    /* First Find i */
    set->first=1;
    while((set->first<=(set->size-2)) && (Mul(set->str, 0, set->first) != 2)) set->first++;
    if (set->first>(set->size-2)) return NO;
    set->second = set->first;
    while(set->second<=(set->size-1) && (Mul(set->str, set->first, set->second) != 3)) set->second++;
    if (set->second>(set->size-1)) return NO;
    if (Mul(set->str, set->second, set->size) != 4) return NO;

    return YES;
}
void ClearAndFreeSet(Dijkstra *set)
{
    if (set->instr) free(set->instr);
    if (set->str) free(set->str);
    set->first = set->second = set->size = set->len = set->xRep = 0;
}
void ClearSet(Dijkstra *set)
{
    set->instr = NULL;
    set->str = NULL;
    set->first = set->second = set->size = set->len = set->xRep = 0;
}
void ExpandString(Dijkstra *set)
{
    set->str = (char *)malloc(set->len*set->xRep+1);
    memset(set->str,0,(set->len*set->xRep+1));
    for(int i=0;i<set->xRep;i++)
        strcat(set->str, set->instr);
    set->size = set->len*set->xRep;
}
void IntTokenize(string word, int *len, int*xRep)
{

 bool exit = false;
 int index=0;
 const char *cstr = word.c_str();
 int num=0;
 int count=0;
 
 while(index<word.length() && !exit)
 {
  if (cstr[index]>='0' && cstr[index]<='9')
      num = num*10 + cstr[index]-'0';
  else if (cstr[index] == ' ')
  {
      *len = num;
      num = 0;
  }
  else
      exit = true;
  index++;
 }
*xRep = num;
}