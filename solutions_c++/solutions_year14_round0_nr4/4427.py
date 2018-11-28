    #include<stdio.h>
    #include<string.h>
    #include<algorithm>
     
    using namespace std;
     
    int T,test,n;
    double arr1[1001],arr2[1001];
    int g[2010][2010],m;
    int arr3[2010];
    int a,b;
     
    bool dfs(int v){
    if(v==m)return 1;
    arr3[v]=1;
    for(int i=0;i<=m;i++)
    if(g[v][i]&&!arr3[i]&&dfs(i)){
    g[v][i]=0;
    g[i][v]=1;
    arr3[v]=0;
    return 1;
    }
    arr3[v]=0;
    return 0;
    }
     
    int main(){
    int i,j;
    scanf("%d",&test);
    while(test--){
    scanf("%d",&n);
    for(i=0;i<n;i++)scanf("%lf",&arr1[i]);
    for(i=0;i<n;i++)scanf("%lf",&arr2[i]);
    sort(arr1,arr1+n);
    sort(arr2,arr2+n);
    m=2*n+1;
     
    memset(g,0,sizeof(g));
    for(i=0;i<n;i++)g[0][1+i]=1;
    for(i=0;i<n;i++)g[1+n+i][m]=1;
    for(i=0;i<n;i++)for(j=0;j<n;j++)
    g[1+i][1+n+j]=(arr1[i]>arr2[j]?1:0);
    for(a=0;dfs(0);a++);
     
    b=0;
    for(i=j=n-1;i>=0;i--){
    if(arr1[i]>arr2[j]){
    b++;
    }else{
    j--;
    }
    }
     
    printf("Case #%d: %d %d\n",++T,a,b);
    }
    return 0;
    }
     
