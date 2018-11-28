from __future__ import print_function
maxdiv = 11
primes = []
primesq = []
power = maxdiv*[0]

def genPrimes():
	primes.append(2)
	primesq.append(4)
	N = (1<<17)
	num  = 3
	while num <= N:
		is_prime = True
		for prime in primes:
			if num % prime == 0:
				is_prime = False
				break
		if isPrime :
			primes.append(num)
			primesq.append(num*num)
		num += 2

def isPrime(num):
	i = 0
	while i < len(primesq) and primesq[i] <= num:
		if num % primes[i] == 0 : return False, primes[i]
		i += 1
	return True, -1

def getAllDivs(numbase2, n):
	div = 2
	divs = maxdiv*[0]
	while div < maxdiv:
		tempnum = 0
		for i in range(n):
			if numbase2[n-i-1]=='1': tempnum += power[div][i]
		prime,_div = isPrime(tempnum)
		if prime : return []
		#print([ tempnum, prime, _div])
		divs[div] = _div
		div += 1
	return divs

def main ():
	genPrimes()
	#print("primes generated")
	#return
	maxj = 500
	maxn = 32 #32
	for x in range(maxdiv):
		power[x] = maxn*[0]
	for x in range(maxdiv):
		b = 1
		for i in range(maxn):
			power[x][i] = b
			b = b*x
	n = 2
	while n <= 32:
		divs = []
		nums = []
		num = (1 << n ) - 1
		minNum = (1<<(n-1)) + 1
		j = 0
		while num >= minNum and j<maxj:
			_divs = getAllDivs(bin(num)[2:], n)
			if len(_divs) != 0 :
				nums.append(num)
				divs.append(_divs[2:])
				j += 1
			num -= 2
		print(n)
		print(len(nums))
		for j in range(len(nums)):
			print(bin(nums[j])[2:], end=" ")
			for div in divs[j]:
				print(div, end=" ")
			print("")
		n += 1

if __name__ == "__main__":
	main()


