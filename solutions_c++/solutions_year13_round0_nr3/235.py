#include<cstdio>
#include<cstring>
#include<algorithm>
#define MAXL 110
using namespace std;

// Palindrome Squares
typedef struct{
  char seq[MAXL];
}NODE;
int cnt;
NODE node[50000];

// Strings
char tmp[MAXL],org[MAXL];

// Range
char A[MAXL],B[MAXL];

// Multiply
void multi(char* s1,char* s2,char* ans)
{
  int i,j,in,now,len1=strlen(s1),len2=strlen(s2);
  memset(tmp,0,(len1+len2)*sizeof(char));
  for(j=len2-1;j>=0;--j)
  {
    for(i=len1-1,in=0;i>=0;--i)
    {
      now=(s1[i]-'0')*(s2[j]-'0')+in;
      in=(tmp[len1+len2-j-i-2]+now)/10;
      tmp[len1+len2-j-i-2]=(tmp[len1+len2-j-i-2]+now)%10;
    }
    if(in) tmp[len1+len2-j-1]=in;
  }
  for(now=len1+len2-1;!tmp[now];--now);
  if(now>=0)
  {
    for(i=0;i<=now;++i) ans[now-i]=tmp[i]+'0';
    ans[now+1]='\0';
  }
  else
  {
    ans[0]='0';
    ans[1]='\0';
  }
}

// Add
void add(char *str)
{
  // str^2
  multi(org,org,node[cnt].seq);
  cnt++;
  return;
}

// Generating 1 Sequence
char lis[MAXL];
void gen(int now,int rem)
{
  int i;

  // Even
  for(i=0;i<now;i++)
    org[i]=org[2*now-i-1]=lis[i];
  org[2*now]='\0';
  add(org);

  // Odd
  for(i=0;i<now;i++)
    org[2*now-i]=lis[i];
  org[2*now+1]='\0';
  org[now]='0';
  add(org);
  org[now]='1';
  add(org);

  // End
  if(now>=25) return;

  // Insert One
  if(rem<4)
  {
    lis[now]='1';
    gen(now+1,rem+1);
  }

  // Insert Zero
  lis[now]='0';
  gen(now+1,rem);
}

// Generating 2 Sequence
void gen2(int now)
{
  int i;

  // Even
  for(i=0;i<now;i++)
    org[i]=org[2*now-i-1]=lis[i];
  org[2*now]='\0';
  add(org);

  // Odd
  for(i=0;i<now;i++)
    org[2*now-i]=lis[i];
  org[2*now+1]='\0';
  org[now]='0';
  add(org);
  org[now]='1';
  add(org);

  // End
  if(now>=25) return;

  // Insert Only Zero
  lis[now]='0';
  gen2(now+1);
}

// Generating 1..2..1 Sequence
void gen3(int now,int rem)
{
  int i;

  // Odd
  for(i=0;i<now;i++)
    org[i]=org[2*now-i]=lis[i];
  org[2*now+1]='\0';
  org[now]='2';
  add(org);

  // End
  if(now>=25) return;

  // Insert One
  if(rem<2)
  {
    lis[now]='1';
    gen3(now+1,rem+1);
  }

  // Insert Zero
  lis[now]='0';
  gen3(now+1,rem);
}

// Compare Function
bool cmp(NODE a,NODE b)
{
  int i,len1,len2;
  len1=strlen(a.seq);
  len2=strlen(b.seq);
  if(len1!=len2) return len1<len2;
  for(i=0;i<len1&&i<len2;i++)
    if(a.seq[i]!=b.seq[i]) return a.seq[i]<b.seq[i];
  return false;
}

// Smaller
bool smaller(char *a,char *b,int len2)
{
  int i,len1;
  len1=strlen(a);
  if(len1!=len2) return len1<len2;
  for(i=0;i<len1;i++)
    if(a[i]!=b[i]) return a[i]<b[i];
  return false;
}

// Bigger
bool bigger(char *a,char *b,int len2)
{
  int i,len1;
  len1=strlen(a);
  if(len1!=len2) return len1>len2;
  for(i=0;i<len1;i++)
    if(a[i]!=b[i]) return a[i]>b[i];
  return false;
}

// Main
int main(void)
{
  int i,tc,cs,l,r,mid,beg,end,len,len2;

  // Preprocess
  sprintf(node[0].seq,"1");
  sprintf(node[1].seq,"4");
  sprintf(node[2].seq,"9");
  cnt=3;

  // Try 1 Pattern
  lis[0]='1';
  gen(1,1);

  // Try 2 Patterns
  lis[0]='2';
  gen2(1);

  // Try 1..2..1 Pattern
  lis[0]='1';
  gen3(1,1);

  // Sort
  sort(node,node+cnt,cmp);

  // Read Input
  scanf("%d",&tc);
  cs=1;
  while(tc--)
  {
    // Range
    scanf("%s",A);
    scanf("%s",B);

    // Binary Search
    printf("Case #%d: ",cs++);
    l=0,r=cnt-1;
    len=strlen(A);
    while(l<r)
    {
      mid=l+(r-l)/2;
      if(smaller(node[mid].seq,A,len)) l=mid+1;
      else r=mid;
    }
    if(smaller(node[r].seq,A,len)) puts("0");
    else
    {
      beg=r;
      l=0,r=cnt-1;
      len=strlen(B);
      while(l<r)
      {
        mid=l+(r-l+1)/2;
        if(bigger(node[mid].seq,B,len)) r=mid-1;
        else l=mid;
      }
      if(bigger(node[l].seq,B,len)) puts("0");
      else
      {
        end=l;
        printf("%d\n",end-beg+1);
      }
    }
  }

  return 0;
}
