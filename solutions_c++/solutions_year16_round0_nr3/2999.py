#include <stdio.h>
#include <math.h>
int main(){
	FILE *f = fopen("outC.txt","wt");
	int T,i;
	scanf("%d",&T);
	for(i=0;i<T;i++){
		fprintf(f,"Case #%d: \n", i+1);
		int N,J;
		unsigned long long number=0,number2=0,number3;
		int divisor[12];
		char strNum[50]={0};
		scanf("%d %d",&N,&J);
		number3=pow(2,N-1)+1;
		long long int forcal=number3;
		int forcal2=0;
		while(forcal>0){
			number+=pow(10,forcal2)*(forcal%2);
			forcal/=2;
			forcal2+=1;
		}
		int count=0, just_count=0,checking = (pow(2,N)-pow(2,N-1)-1)/2+1;
		while(count<J && just_count<checking){
			number2=0;
			sprintf(strNum,"%llu",number);
			for(int i2=0;i2<N;i2++){
				number2+=pow(2,i2)*(strNum[N-1-i2]-48);
			}
			for(int j2=1;j2*j2<number2;j2++){
				//if(j2>3) j2+=1;
				if(number2%j2==0){
					divisor[2]=j2;
					if(divisor[2]>1) break;
				}
			}
			if(divisor[2]!=1){
				number2=0;
				for(int i3=0;i3<N;i3++){
					number2+=pow(3,i3)*(strNum[N-1-i3]-48);
				}
				for(int j3=1;j3*j3<number2;j3++){
					//if(j3>3) j3+=1;
					if(number2%j3==0){
						divisor[3]=j3;
						if(divisor[3]>1) break;
					}
				}
				if(divisor[3]!=1){
					number2=0;
					for(int i4=0;i4<N;i4++){
						number2+=pow(4,i4)*(strNum[N-1-i4]-48);
					}
					for(int j4=1;j4*j4<number2;j4++){
						//if(j4>3) j4+=1;
						if(number2%j4==0){
							divisor[4]=j4;
							if(divisor[4]>1) break;
						}
					}
					if(divisor[4]!=1){
						number2=0;
						for(int i5=0;i5<N;i5++){
							number2+=pow(5,i5)*(strNum[N-1-i5]-48);
						}
						for(int j5=1;j5*j5<number2;j5++){
							//if(j5>3) j5+=1;
							if(number2%j5==0){
								divisor[5]=j5;
								if(divisor[5]>1) break;
							}
						}
						if(divisor[5]!=1){
							number2=0;
							for(int i6=0;i6<N;i6++){
								number2+=pow(6,i6)*(strNum[N-1-i6]-48);
							}
							for(int j6=1;j6*j6<number2;j6++){
								//if(j6>3) j6+=1;
								if(number2%j6==0){
									divisor[6]=j6;
									if(divisor[6]>1) break;
								}
							}
							if(divisor[6]!=1){
								number2=0;
								for(int i7=0;i7<N;i7++){
									number2+=pow(7,i7)*(strNum[N-1-i7]-48);
								}
								for(int j7=1;j7*j7<number2;j7++){
									//if(j7>3) j7+=1;
									if(number2%j7==0){
										divisor[7]=j7;
										if(divisor[7]>1) break;
									}
								}
								if(divisor[7]!=1){
									number2=0;
									for(int i8=0;i8<N;i8++){
										number2+=pow(8,i8)*(strNum[N-1-i8]-48);
									}
									for(int j8=1;j8*j8<number2;j8++){
										//if(j8>3) j8+=1;
										if(number2%j8==0){
											divisor[8]=j8;
											if(divisor[8]>1) break;
										}
									}
									if(divisor[8]!=1){
										number2=0;
										for(int i9=0;i9<N;i9++){
											number2+=pow(9,i9)*(strNum[N-1-i9]-48);
										}
										for(int j9=1;j9*j9<number2;j9++){
											//if(j9>3) j9+=1;
											if(number2%j9==0){
												divisor[9]=j9;
												if(divisor[9]>1) break;
											}
										}
										if(divisor[9]!=1){
											number2=0;
											for(int i0=0;i0<N;i0++){
												number2+=pow(10,i0)*(strNum[N-1-i0]-48);
											}
											for(int j0=1;j0*j0<number2;j0++){
												//if(j0>3) j0+=1;
												if(number2%j0==0){
													divisor[10]=j0;
													if(divisor[10]>1) break;
												}
											}
											if(divisor[10]!=1){
												count+=1;
												printf("%llu %d %d %d %d %d %d %d %d %d\n", number,divisor[2],divisor[3],divisor[4],divisor[5],divisor[6],divisor[7],divisor[8],divisor[9],divisor[10]);
												fprintf(f,"%llu %d %d %d %d %d %d %d %d %d\n", number,divisor[2],divisor[3],divisor[4],divisor[5],divisor[6],divisor[7],divisor[8],divisor[9],divisor[10]);
											}
										}
									}
								}
							}
						}
					}
				}
			}
			number3+=2;
			forcal=number3;
			forcal2=0;
			number=0;
			while(forcal>0){
				number+=pow(10,forcal2)*(forcal%2);
				forcal/=2;
				forcal2+=1;
			}
			just_count+=1;
		}
	}
	fclose(f);
}