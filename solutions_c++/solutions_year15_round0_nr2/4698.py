#include<iostream>

using namespace std;

int dinerA[1500],dinerB[1500],ansB,ansA;
int shiftCostA[1500],shiftCostB[1500];

bool roundB(int maxD){	//end or not
	int maxDiner=0, maxCount=0;
	for(int i=0; i<maxD; i++){
		//maxDiner = diner[maxDiner]<diner[i]?i:maxDiner;
		if(dinerB[maxDiner]<dinerB[i]){
			maxDiner=i;
			maxCount=shiftCostB[maxDiner];
		}else if(dinerB[maxDiner]==dinerB[i]){
			maxCount+=shiftCostB[i];	//shift�j�ܰ�!!  �Ʊ椣�n�ñ�
		}
	}
	//���maxDiner����A�Ҽ{�n���n�N��/2
	if(dinerB[maxDiner]%2!=0){	//�_�� or 8888 -> 4444 = 4min OK, 88888-> 44444 = 5min+4 -> notOK
		for(int i=0; i<maxD; i++){
			if(dinerB[i]!=0) dinerB[i]--;	//���Q�n�X�{�t��
		}
		for(int i=0; i<maxD; i++){
			if(dinerB[i]!=0) return 0;
		}
		return 1;	//�Ҧ��H���O0�F-> end
	}
	if(dinerB[maxDiner]/2+shiftCostB[maxDiner]<dinerB[maxDiner] && dinerB[maxDiner]/2>maxCount){	//�|�L�Ǥp�Ҥl�A�����A-1 �� -1�A�� �����ƬO�@�˪�
		//�n/2
		dinerB[maxDiner]/=2;
		ansB+=shiftCostB[maxDiner]-1;
		shiftCostB[maxDiner]*=2;	//�u��shift�@�� (���æb�~�����@�b�Ʀr���쥻��diner����shift�ĤG��) �C��shift+1 cost
		return 0;
	}else{
		for(int i=0; i<maxD; i++){
			if(dinerB[i]!=0) dinerB[i]--;	//���Q�n�X�{�t��
		}
		for(int i=0; i<maxD; i++){
			if(dinerB[i]!=0) return 0;
		}
		return 1;	//�Ҧ��H���O0�F-> end
	}
}

bool roundA(int maxD){	//end or not
	int maxDiner=0, maxCount=0, secondDiner=0;
	for(int i=0; i<maxD; i++){
		//maxDiner = diner[maxDiner]<diner[i]?i:maxDiner;
		if(dinerA[maxDiner]<dinerA[i]){
			maxDiner=i;
			maxCount=shiftCostA[maxDiner];
		}else if(dinerA[maxDiner]==dinerA[i]){
			maxCount+=shiftCostA[i];	//shift�j�ܰ�!!  �Ʊ椣�n�ñ�
		}
	}
	//���maxDiner����A�Ҽ{�n���n�N��/2
	int div=1, addMin=10000;
	for(int i=1; i<=dinerA[maxDiner]/2; i++){
		if(dinerA[maxDiner]%i!=0) continue;	//�����i�N����
		//addMin=min(addMin,i+diner[maxDiner]/i);
		if(addMin>=i+(dinerA[maxDiner]/i-1)*maxCount){
			addMin = i+(dinerA[maxDiner]/i-1)*maxCount;
			div = i;
		}//div�O�̫�Ʀr
	}		

		//splitCost           * �Ӽ�   + �ѤUcake�ƶq(min) < �쥻min
	if((dinerA[maxDiner]/div-1)*maxCount+			div		<dinerA[maxDiner]-1){	//�|�L�Ǥp�Ҥl�A�����A-1 �� -1�A�� �����ƬO�@�˪�
		ansA+=(dinerA[maxDiner]/div-1);
		shiftCostA[maxDiner]+=(dinerA[maxDiner]/div-1);	//�u��shift�@�� (���æb�~�����@�b�Ʀr���쥻��diner����shift�ĤG��) �C��shift+1 cost
		dinerA[maxDiner]=div;	// 9/3 = 3, splitCost 2
		return 0;
	}else{
		ansA++;
		for(int i=0; i<maxD; i++){
			if(dinerA[i]!=0) dinerA[i]--;	//���Q�n�X�{�t��
		}
		for(int i=0; i<maxD; i++){
			if(dinerA[i]!=0) return 0;
		}
		return 1;	//�Ҧ��H���O0�F-> end
	}
}

int main(){
	int cases, diners, maxCake;
	cin>>cases;
	for(int c=1; c<=cases; c++){
		ansA=0; maxCake=0; ansB=0;
		cin>>diners;
		for(int i=0; i<diners; i++){ shiftCostA[i]=1; shiftCostB[i]=1; }
		for(int i=0; i<diners; i++){
			cin>>dinerA[i];
			if(dinerA[i]>maxCake) maxCake=dinerA[i];
		}
		memcpy(dinerB,dinerA,sizeof(dinerA));
		while(!roundA(diners)) ;
		ansB++;
		while(!roundB(diners)) ansB++;
		if(ansA>maxCake) ansA=maxCake;
		if(ansB>maxCake) ansB=maxCake;
		if(ansA>ansB) cout<<"Case #"<<c<<": "<<ansB<<endl;
		else cout<<"Case #"<<c<<": "<<ansA<<endl;
		
	}
	return 0;
}