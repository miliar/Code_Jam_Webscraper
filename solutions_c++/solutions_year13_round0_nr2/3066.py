/*
1.���] YES 
   (1)�p�G ���@�Ci ��������a(i,j) �b�Ӧ榳��L�j�� => �����ӳQ ����(colemn) mow;
      so ���ઽ�A�����(�@�檺��C�Ҧ��񥦤j����) => NO 
2.�p�G�OK && ����OK => �i�Hmow�X�Ӯ� 
 
*/
#include<iostream>
using namespace std;
int main(void)
{
   int T,N,M;
   int i,j,k;
   cin >> T;
   for(i=1;i<=T;i++){
      cin >> N >> M;
      short LP[N][M];// lawn_pattern
      short max_i[N],max_j[M];
      // 
      for(j=0;j<N;j++){
         max_i[j]=0; 
         for(k=0;k<M;k++){
            cin >> *(*(LP+j)+k);
            if(*(*(LP+j)+k) > max_i[j])
               max_i[j]=*(*(LP+j)+k); 
         }
      }
      for(k=0;k<M;k++){
         max_j[k]=0;
         for(j=0;j<N;j++){
            if(*(*(LP+j)+k) > max_j[k])
               max_j[k]=*(*(LP+j)+k);
         }
      }
      // (1)
      short ans=0;//0:YES, 1:NO
      for(j=0;j<N && (!ans);j++){
         for(k=0;k<M && (!ans);k++){
            if(*(*(LP+j)+k)<max_i[j] && *(*(LP+j)+k)<max_j[k]){
               // 1.(1)
               ans=1;
            }
         }
      }
      //
      cout << "Case #" << i << ": ";
      if(!ans)
         cout << "YES";
      else if(ans==1)
         cout << "NO";
      cout << endl;
   }
   return 0;
}
