#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int T;
    scanf("%d",&T);//��J�`�@�X��CASE 
    for(int t=1;t<=T;t++)
    {
        int *array;
        int n;
        scanf("%d",&n);//��J�`�۵��Ū��� 
        array = new int [n+1];
        char str[n];
        scanf("%s",str);//��J�C�ӤH���`�۵��� 
        for(int i=0;i<=n;i++)//��l�� 
        {      
           //array[i]=atoi(str);
           array[i]=int(str[i]- '0');
        }
   
        //�C�ӤH���h�ˬd 
        int M=0;//�ثe���_�Ӫ��H�� 
        int G=0; //�ٮt�h�֤H 
        for(int i=0;i<=n;i++)
        {   
           if(array[i]!=0){ 
               if(M >= i)//�ˬd�O�_��i�ӤH���_��
               {         
                   M += array[i];  
               } 
               else{
                   G += i-M; //���H�� 
                   M += array[i]+G;//�����˦��H���[�i�h 
               }
           }
        }   
        printf("Case #%d: %d\n",t,G);       
        delete [] array;
    }
    
    

    system("PAUSE");
    return 0;
}
