#include <stdio.h>
#include <math.h>
#include <iostream>
int main()
{
     freopen("22.in","r",stdin); //�����ض����������ݽ���in.txt�ļ��ж�ȡ
    freopen("22.out","w",stdout); //����ض���������ݽ�������out.txt�ļ���

    int T;
    scanf("%d",&T);
    for(int testcase=1;testcase<=T;testcase++){
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double res = 0;
        for(int i = 0;;i++ ){
            double curend =res+x/(2+f*i);
            double nextend = res+c/(2+f*i)+x/(2+f*(i+1));
            if(curend<=nextend){
                res=curend;
                break;
            }else{
                res=res+c/(2+f*i);
            }
        }
        printf("Case #%d: %.7f\n",testcase,res);

    }
    fclose(stdin);//�ر��ļ�
    fclose(stdout);//�ر��ļ�
    return 0;
}
